# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maps.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='maps.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nmaps.proto\".\n\x0bMAPSRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\toffice_no\x18\x02 \x01(\t\"\x1c\n\tMAPSReply\x12\x0f\n\x07message\x18\x01 \x01(\t2<\n\x0bMAPS_server\x12-\n\x0fValidatePatient\x12\x0c.MAPSRequest\x1a\n.MAPSReply\"\x00\x62\x06proto3')
)




_MAPSREQUEST = _descriptor.Descriptor(
  name='MAPSRequest',
  full_name='MAPSRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='MAPSRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='office_no', full_name='MAPSRequest.office_no', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=14,
  serialized_end=60,
)


_MAPSREPLY = _descriptor.Descriptor(
  name='MAPSReply',
  full_name='MAPSReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='MAPSReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=62,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['MAPSRequest'] = _MAPSREQUEST
DESCRIPTOR.message_types_by_name['MAPSReply'] = _MAPSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MAPSRequest = _reflection.GeneratedProtocolMessageType('MAPSRequest', (_message.Message,), dict(
  DESCRIPTOR = _MAPSREQUEST,
  __module__ = 'maps_pb2'
  # @@protoc_insertion_point(class_scope:MAPSRequest)
  ))
_sym_db.RegisterMessage(MAPSRequest)

MAPSReply = _reflection.GeneratedProtocolMessageType('MAPSReply', (_message.Message,), dict(
  DESCRIPTOR = _MAPSREPLY,
  __module__ = 'maps_pb2'
  # @@protoc_insertion_point(class_scope:MAPSReply)
  ))
_sym_db.RegisterMessage(MAPSReply)



_MAPS_SERVER = _descriptor.ServiceDescriptor(
  name='MAPS_server',
  full_name='MAPS_server',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=92,
  serialized_end=152,
  methods=[
  _descriptor.MethodDescriptor(
    name='ValidatePatient',
    full_name='MAPS_server.ValidatePatient',
    index=0,
    containing_service=None,
    input_type=_MAPSREQUEST,
    output_type=_MAPSREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAPS_SERVER)

DESCRIPTOR.services_by_name['MAPS_server'] = _MAPS_SERVER

# @@protoc_insertion_point(module_scope)
