# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getTime.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rgetTime.proto\x12\x07getTime\"\xec\x01\n\x0bTimeRequest\x12)\n\x02tz\x18\x01 \x01(\x0e\x32\x1d.getTime.TimeRequest.timeZone\"\xb1\x01\n\x08timeZone\x12\x06\n\x02\x41\x42\x10\x00\x12\x06\n\x02\x41\x44\x10\x01\x12\x07\n\x03\x41\x44\x43\x10\x02\x12\x06\n\x02\x41\x45\x10\x03\x12\x06\n\x02\x41J\x10\x04\x12\x07\n\x03\x41LA\x10\x05\x12\x06\n\x02\x41M\x10\x06\x12\x07\n\x03\x41SI\x10\x07\x12\x06\n\x02\x41S\x10\x08\x12\x06\n\x02\x41T\x10\t\x12\x06\n\x02\x41V\x10\n\x12\x06\n\x02\x41W\x10\x0b\x12\x06\n\x02\x43P\x10\x0c\x12\x06\n\x02\x43Y\x10\r\x12\x07\n\x03MBN\x10\x0e\x12\x0b\n\x07PST8PDT\x10\x0f\x12\x07\n\x03USP\x10\x10\x12\x08\n\x04USPN\x10\x11\x12\t\n\x05\x45UBlN\x10\x12\"<\n\tTimeOfDay\x12\r\n\x05hours\x18\x01 \x01(\x05\x12\x0f\n\x07minutes\x18\x02 \x01(\x05\x12\x0f\n\x07seconds\x18\x03 \x01(\x05\x32\x44\n\x07getTime\x12\x39\n\rGetTimeAtZone\x12\x14.getTime.TimeRequest\x1a\x12.getTime.TimeOfDayb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'getTime_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TIMEREQUEST._serialized_start=27
  _TIMEREQUEST._serialized_end=263
  _TIMEREQUEST_TIMEZONE._serialized_start=86
  _TIMEREQUEST_TIMEZONE._serialized_end=263
  _TIMEOFDAY._serialized_start=265
  _TIMEOFDAY._serialized_end=325
  _GETTIME._serialized_start=327
  _GETTIME._serialized_end=395
# @@protoc_insertion_point(module_scope)