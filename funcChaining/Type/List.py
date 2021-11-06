import functools
from funcChaining.Type.BaseType import BaseType


class List(BaseType, list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def pack(cls, obj):
        return cls(obj)

    def map(self, func):
        return List(map(func, self))

    def filter(self, func):
        return List(filter(func, self))

    def reduce(self, func, initial=None):
        return functools.reduce(func, self, initial)
