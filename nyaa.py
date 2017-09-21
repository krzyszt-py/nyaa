"""
Import torrents from nyaatorrents.ue
"""
import argparse
import gzip
import logging
import os
import re
import shutil
import time

import feedparser
import requests
from nyaa_pb2 import (DB, Torrent)
from typing import List, Iterable, Set

parser = argparse.ArgumentParser('Anime nyaa')

# config
parser.add_argument('--torrent_dir', default='/home/krzyszt/')
parser.add_argument('--db_path', default='/home/krzyszt/.config')
parser.add_argument('--db_file', default='nyaa.pb.gz')

# runtime args
parser.add_argument('--add_rss')
parser.add_argument('--del_rss')
parser.add_argument('--add_anime', nargs='+')
parser.add_argument('--del_anime')
parser.add_argument('--info', '-i', action='count', default=0)

config = parser.parse_args()
LOGGER = logging.getLogger('nyaa')


def get_torrents(rss: str) -> List[Torrent]:
    """Search for torrents in RSS"""

    feed = feedparser.parse(rss)
    return [Torrent(id=0,
                    url=torrent['link'],
                    name=torrent['title'],
                    published=int(time.mktime(torrent['published_parsed'])))
            for torrent in feed['items']]


def save_torrent(torrent: Torrent) -> None:
    """Download and save file (torrent)"""

    path = os.path.join(os.path.abspath('.'), config.torrent_dir)
    if not os.path.exists(path):
        os.mkdir(path)
    torrent_content = requests.get(torrent.url).content
    with open('/tmp/anime.torrent', 'wb') as writer:
        writer.write(torrent_content)
        shutil.move('/tmp/anime.torrent', os.path.join(path, torrent.name))


def load_db() -> DB:
    db = DB()
    path = os.path.join(config.db_path, config.db_file)
    if os.path.exists(path):
        with gzip.open(path, 'rb') as fd:
            db.ParseFromString(fd.read())
        LOGGER.debug('connected to db')
    return db


def store_db(db) -> None:
    path = os.path.join(config.db_path, config.db_file)
    with gzip.open(path, 'wb') as fd:
        fd.write(db.SerializeToString())


def add_rss(rss: str) -> None:
    db = load_db()

    new_rss = db.rss.add()
    ids = set()
    for i in db.rss:
        ids.add(i.id)
        if i.url == rss:
            LOGGER.info('RSS: %s already exists', rss)
            return

    new_rss.id = min(set(range(max(ids) + 2)) - ids)
    new_rss.url = rss
    LOGGER.info('New RSS added: (%s, %d)', rss, new_rss.id)

    store_db(db)


def info(done=False):
    db = load_db()

    LOGGER.info('RSS:')
    for rss in db.rss:
        LOGGER.info('  - %d: %s', rss.id, rss.url)

    LOGGER.info('Anime:')
    for anime in db.anime:
        LOGGER.info('  - %d: [%s] %s', anime.id, anime.group, ' '.join(anime.title))

    if done:
        LOGGER.info('Done:')
        for done in db.done:
            LOGGER.info('  - %s', done.name)



def max_id(x: Iterable) -> int:
    ids = set(i.id for i in x)
    return min(set(range(max(ids) + 2)) - ids)


def add_anime(anime: List[str]) -> None:
    db = load_db()
    group, *title = anime
    anime = db.anime.add()
    anime.id = max_id(db.anime)
    anime.group = group
    anime.title.extend(title)
    store_db(db)


def del_anime(anime_id: str):
    db = load_db()
    for anime in db.anime[:]:
        if anime.id == int(anime_id):
            db.anime.remove(anime)
    store_db(db)

def del_rss(rss_id: str):
    db = load_db()
    for rss in db.rss[:]:
        if rss.id == int(rss_id):
            db.rss.remove(rss)
    store_db(db)


def main():
    """start db, parse pages and download torrents"""

    db = load_db()
    EXP = re.compile('(' +
                     ')|('.join('.*'.join([anime.group] + list(anime.title))
                                for anime in db.anime) +
                     ')', re.I)
    LOGGER.debug(EXP.pattern)
    done: Set[Torrent] = {d.url for d in db.done}

    for rss in db.rss:
        for torrent in get_torrents(rss.url):
            if EXP.search(torrent.name) and torrent.url not in done:
                db.done.extend([torrent])
                save_torrent(torrent)
                LOGGER.info('torrent saved: %s', torrent.name)
    store_db(db)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if config.add_rss:
        add_rss(config.add_rss)
    elif config.del_rss:
        del_rss(config.del_rss)
    elif config.add_anime:
        add_anime(config.add_anime)
    elif config.del_anime:
        del_anime(config.del_anime)
    elif config.info:
        logging.basicConfig(level=logging.DEBUG)
        info(config.info > 1)
    else:
        main()
