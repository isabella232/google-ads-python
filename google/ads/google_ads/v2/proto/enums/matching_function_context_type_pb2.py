# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/enums/matching_function_context_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/enums/matching_function_context_type.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v2.enumsB MatchingFunctionContextTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums'),
  serialized_pb=_b('\nHgoogle/ads/googleads_v2/proto/enums/matching_function_context_type.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\x81\x01\n\x1fMatchingFunctionContextTypeEnum\"^\n\x1bMatchingFunctionContextType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x10\n\x0c\x46\x45\x45\x44_ITEM_ID\x10\x02\x12\x0f\n\x0b\x44\x45VICE_NAME\x10\x03\x42\xf5\x01\n!com.google.ads.googleads.v2.enumsB MatchingFunctionContextTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MATCHINGFUNCTIONCONTEXTTYPEENUM_MATCHINGFUNCTIONCONTEXTTYPE = _descriptor.EnumDescriptor(
  name='MatchingFunctionContextType',
  full_name='google.ads.googleads.v2.enums.MatchingFunctionContextTypeEnum.MatchingFunctionContextType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEED_ITEM_ID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_NAME', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=173,
  serialized_end=267,
)
_sym_db.RegisterEnumDescriptor(_MATCHINGFUNCTIONCONTEXTTYPEENUM_MATCHINGFUNCTIONCONTEXTTYPE)


_MATCHINGFUNCTIONCONTEXTTYPEENUM = _descriptor.Descriptor(
  name='MatchingFunctionContextTypeEnum',
  full_name='google.ads.googleads.v2.enums.MatchingFunctionContextTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MATCHINGFUNCTIONCONTEXTTYPEENUM_MATCHINGFUNCTIONCONTEXTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=267,
)

_MATCHINGFUNCTIONCONTEXTTYPEENUM_MATCHINGFUNCTIONCONTEXTTYPE.containing_type = _MATCHINGFUNCTIONCONTEXTTYPEENUM
DESCRIPTOR.message_types_by_name['MatchingFunctionContextTypeEnum'] = _MATCHINGFUNCTIONCONTEXTTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchingFunctionContextTypeEnum = _reflection.GeneratedProtocolMessageType('MatchingFunctionContextTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _MATCHINGFUNCTIONCONTEXTTYPEENUM,
  __module__ = 'google.ads.googleads_v2.proto.enums.matching_function_context_type_pb2'
  ,
  __doc__ = """Container for context types for an operand in a matching function.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.MatchingFunctionContextTypeEnum)
  ))
_sym_db.RegisterMessage(MatchingFunctionContextTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)