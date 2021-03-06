# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nyaa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nyaa.proto',
  package='nyaa',
  syntax='proto3',
  serialized_pb=_b('\n\nnyaa.proto\x12\x04nyaa\"C\n\x07Torrent\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tpublished\x18\x04 \x01(\x02\"\x1e\n\x03Rss\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0b\n\x03url\x18\x02 \x01(\t\"1\n\x05\x41nime\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05group\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x03(\t\"U\n\x02\x44\x42\x12\x16\n\x03rss\x18\x01 \x03(\x0b\x32\t.nyaa.Rss\x12\x1a\n\x05\x61nime\x18\x02 \x03(\x0b\x32\x0b.nyaa.Anime\x12\x1b\n\x04\x64one\x18\x03 \x03(\x0b\x32\r.nyaa.Torrentb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TORRENT = _descriptor.Descriptor(
  name='Torrent',
  full_name='nyaa.Torrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nyaa.Torrent.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='nyaa.Torrent.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='nyaa.Torrent.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='published', full_name='nyaa.Torrent.published', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=87,
)


_RSS = _descriptor.Descriptor(
  name='Rss',
  full_name='nyaa.Rss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nyaa.Rss.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='nyaa.Rss.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=119,
)


_ANIME = _descriptor.Descriptor(
  name='Anime',
  full_name='nyaa.Anime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nyaa.Anime.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='nyaa.Anime.group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='nyaa.Anime.title', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=170,
)


_DB = _descriptor.Descriptor(
  name='DB',
  full_name='nyaa.DB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rss', full_name='nyaa.DB.rss', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anime', full_name='nyaa.DB.anime', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='done', full_name='nyaa.DB.done', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=257,
)

_DB.fields_by_name['rss'].message_type = _RSS
_DB.fields_by_name['anime'].message_type = _ANIME
_DB.fields_by_name['done'].message_type = _TORRENT
DESCRIPTOR.message_types_by_name['Torrent'] = _TORRENT
DESCRIPTOR.message_types_by_name['Rss'] = _RSS
DESCRIPTOR.message_types_by_name['Anime'] = _ANIME
DESCRIPTOR.message_types_by_name['DB'] = _DB

Torrent = _reflection.GeneratedProtocolMessageType('Torrent', (_message.Message,), dict(
  DESCRIPTOR = _TORRENT,
  __module__ = 'nyaa_pb2'
  # @@protoc_insertion_point(class_scope:nyaa.Torrent)
  ))
_sym_db.RegisterMessage(Torrent)

Rss = _reflection.GeneratedProtocolMessageType('Rss', (_message.Message,), dict(
  DESCRIPTOR = _RSS,
  __module__ = 'nyaa_pb2'
  # @@protoc_insertion_point(class_scope:nyaa.Rss)
  ))
_sym_db.RegisterMessage(Rss)

Anime = _reflection.GeneratedProtocolMessageType('Anime', (_message.Message,), dict(
  DESCRIPTOR = _ANIME,
  __module__ = 'nyaa_pb2'
  # @@protoc_insertion_point(class_scope:nyaa.Anime)
  ))
_sym_db.RegisterMessage(Anime)

DB = _reflection.GeneratedProtocolMessageType('DB', (_message.Message,), dict(
  DESCRIPTOR = _DB,
  __module__ = 'nyaa_pb2'
  # @@protoc_insertion_point(class_scope:nyaa.DB)
  ))
_sym_db.RegisterMessage(DB)


# @@protoc_insertion_point(module_scope)
