from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeOfDay(_message.Message):
    __slots__ = ["hours", "minutes", "seconds"]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    hours: int
    minutes: int
    seconds: int
    def __init__(self, hours: _Optional[int] = ..., minutes: _Optional[int] = ..., seconds: _Optional[int] = ...) -> None: ...

class TimeRequest(_message.Message):
    __slots__ = ["tz"]
    class timeZone(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AB: TimeRequest.timeZone
    AD: TimeRequest.timeZone
    ADC: TimeRequest.timeZone
    AE: TimeRequest.timeZone
    AJ: TimeRequest.timeZone
    ALA: TimeRequest.timeZone
    AM: TimeRequest.timeZone
    AS: TimeRequest.timeZone
    ASI: TimeRequest.timeZone
    AT: TimeRequest.timeZone
    AV: TimeRequest.timeZone
    AW: TimeRequest.timeZone
    CP: TimeRequest.timeZone
    CY: TimeRequest.timeZone
    EUBlN: TimeRequest.timeZone
    MBN: TimeRequest.timeZone
    PST8PDT: TimeRequest.timeZone
    TZ_FIELD_NUMBER: _ClassVar[int]
    USP: TimeRequest.timeZone
    USPN: TimeRequest.timeZone
    tz: TimeRequest.timeZone
    def __init__(self, tz: _Optional[_Union[TimeRequest.timeZone, str]] = ...) -> None: ...
