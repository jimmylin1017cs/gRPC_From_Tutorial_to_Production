# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app.proto',
  package='rpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\tapp.proto\x12\x03rpc\";\n\x08StoreReq\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\x0c\x12\x15\n\raccount_token\x18\x03 \x01(\t\"\x0b\n\tStoreResp\"\x15\n\x06GetReq\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x16\n\x07GetResp\x12\x0b\n\x03val\x18\x01 \x01(\x0c\"\x07\n\x05\x45mpty\"\x16\n\x05Image\x12\r\n\x05image\x18\x01 \x01(\x0c\"\x1e\n\rGetByTokenReq\x12\r\n\x05token\x18\x01 \x01(\t\"/\n\x0eGetByTokenResp\x12\x1d\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x0c.rpc.Account\"\'\n\x07\x41\x63\x63ount\x12\x1c\n\x14max_StreamVideo_keys\x18\x01 \x01(\x03\x32U\n\x05\x43\x61\x63he\x12(\n\x05Store\x12\r.rpc.StoreReq\x1a\x0e.rpc.StoreResp\"\x00\x12\"\n\x03Get\x12\x0b.rpc.GetReq\x1a\x0c.rpc.GetResp\"\x00\x32\x35\n\x0bStreamVideo\x12&\n\x08GetVideo\x12\n.rpc.Empty\x1a\n.rpc.Image\"\x00\x30\x01\x32\x43\n\x08\x41\x63\x63ounts\x12\x37\n\nGetByToken\x12\x12.rpc.GetByTokenReq\x1a\x13.rpc.GetByTokenResp\"\x00\x62\x06proto3'
)




_STOREREQ = _descriptor.Descriptor(
  name='StoreReq',
  full_name='rpc.StoreReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='rpc.StoreReq.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val', full_name='rpc.StoreReq.val', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_token', full_name='rpc.StoreReq.account_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=77,
)


_STORERESP = _descriptor.Descriptor(
  name='StoreResp',
  full_name='rpc.StoreResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=90,
)


_GETREQ = _descriptor.Descriptor(
  name='GetReq',
  full_name='rpc.GetReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='rpc.GetReq.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=113,
)


_GETRESP = _descriptor.Descriptor(
  name='GetResp',
  full_name='rpc.GetResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='rpc.GetResp.val', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=137,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='rpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=146,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='rpc.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='rpc.Image.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=170,
)


_GETBYTOKENREQ = _descriptor.Descriptor(
  name='GetByTokenReq',
  full_name='rpc.GetByTokenReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='rpc.GetByTokenReq.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=202,
)


_GETBYTOKENRESP = _descriptor.Descriptor(
  name='GetByTokenResp',
  full_name='rpc.GetByTokenResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='rpc.GetByTokenResp.account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=251,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='rpc.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_StreamVideo_keys', full_name='rpc.Account.max_StreamVideo_keys', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=292,
)

_GETBYTOKENRESP.fields_by_name['account'].message_type = _ACCOUNT
DESCRIPTOR.message_types_by_name['StoreReq'] = _STOREREQ
DESCRIPTOR.message_types_by_name['StoreResp'] = _STORERESP
DESCRIPTOR.message_types_by_name['GetReq'] = _GETREQ
DESCRIPTOR.message_types_by_name['GetResp'] = _GETRESP
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['GetByTokenReq'] = _GETBYTOKENREQ
DESCRIPTOR.message_types_by_name['GetByTokenResp'] = _GETBYTOKENRESP
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StoreReq = _reflection.GeneratedProtocolMessageType('StoreReq', (_message.Message,), {
  'DESCRIPTOR' : _STOREREQ,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.StoreReq)
  })
_sym_db.RegisterMessage(StoreReq)

StoreResp = _reflection.GeneratedProtocolMessageType('StoreResp', (_message.Message,), {
  'DESCRIPTOR' : _STORERESP,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.StoreResp)
  })
_sym_db.RegisterMessage(StoreResp)

GetReq = _reflection.GeneratedProtocolMessageType('GetReq', (_message.Message,), {
  'DESCRIPTOR' : _GETREQ,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.GetReq)
  })
_sym_db.RegisterMessage(GetReq)

GetResp = _reflection.GeneratedProtocolMessageType('GetResp', (_message.Message,), {
  'DESCRIPTOR' : _GETRESP,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.GetResp)
  })
_sym_db.RegisterMessage(GetResp)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Empty)
  })
_sym_db.RegisterMessage(Empty)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Image)
  })
_sym_db.RegisterMessage(Image)

GetByTokenReq = _reflection.GeneratedProtocolMessageType('GetByTokenReq', (_message.Message,), {
  'DESCRIPTOR' : _GETBYTOKENREQ,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.GetByTokenReq)
  })
_sym_db.RegisterMessage(GetByTokenReq)

GetByTokenResp = _reflection.GeneratedProtocolMessageType('GetByTokenResp', (_message.Message,), {
  'DESCRIPTOR' : _GETBYTOKENRESP,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.GetByTokenResp)
  })
_sym_db.RegisterMessage(GetByTokenResp)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'app_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Account)
  })
_sym_db.RegisterMessage(Account)



_CACHE = _descriptor.ServiceDescriptor(
  name='Cache',
  full_name='rpc.Cache',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=294,
  serialized_end=379,
  methods=[
  _descriptor.MethodDescriptor(
    name='Store',
    full_name='rpc.Cache.Store',
    index=0,
    containing_service=None,
    input_type=_STOREREQ,
    output_type=_STORERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='rpc.Cache.Get',
    index=1,
    containing_service=None,
    input_type=_GETREQ,
    output_type=_GETRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CACHE)

DESCRIPTOR.services_by_name['Cache'] = _CACHE


_STREAMVIDEO = _descriptor.ServiceDescriptor(
  name='StreamVideo',
  full_name='rpc.StreamVideo',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=381,
  serialized_end=434,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetVideo',
    full_name='rpc.StreamVideo.GetVideo',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_IMAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMVIDEO)

DESCRIPTOR.services_by_name['StreamVideo'] = _STREAMVIDEO


_ACCOUNTS = _descriptor.ServiceDescriptor(
  name='Accounts',
  full_name='rpc.Accounts',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=436,
  serialized_end=503,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetByToken',
    full_name='rpc.Accounts.GetByToken',
    index=0,
    containing_service=None,
    input_type=_GETBYTOKENREQ,
    output_type=_GETBYTOKENRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTS)

DESCRIPTOR.services_by_name['Accounts'] = _ACCOUNTS

# @@protoc_insertion_point(module_scope)
