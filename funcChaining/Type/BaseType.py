from typing import overload


class BaseType:
    @overload
    @classmethod
    def pack(cls, obj):
        return NotImplemented
