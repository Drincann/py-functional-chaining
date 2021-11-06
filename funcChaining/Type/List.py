import functools
from typing import Callable, Iterable, SupportsIndex, TypeVar, overload
from funcChaining.Type.BaseType import BaseType
from .GenericType import GenericType

_T = TypeVar('_T')


class List(BaseType, list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 实现 BaseType
    @classmethod
    def pack(cls, obj):
        # 这里留作将来可能的扩展
        return cls(obj)

    # 函数式方法
    def map(self, func):
        return List(map(func, self))

    def filter(self, func):
        return List(filter(func, self))

    def reduce(self, func, initial=None):
        return functools.reduce(func, self, initial)

    def zip(self, *iterables: Iterable[_T]) -> "List":
        return List(zip(self, *iterables))

    # 原有方法的包装
    # 质变方法
    def clear(self) -> "List":
        super().clear()
        return self

    def insert(self, __index, __object: _T) -> "List":
        super().insert(__index, __object)
        return self

    def append(self, __object: _T) -> "List":
        super().append(__object)
        return self

    def pop(self, __index=...) -> "List":
        super().pop(__index=__index)
        return self

    def extend(self, __iterable) -> "List":
        super().extend(__iterable)
        return self

    def remove(self, __value: _T) -> "List":
        super().remove(__value)
        return self

    def reverse(self) -> None:
        super().reverse()
        return self

    def sort(self, *, key: Callable, reverse: bool = ...) -> None:
        super().sort(self, key=key, reverse=reverse)
        return self

    # 非质变方法
    def copy(self) -> "List":
        return List(super().copy())

    def index(self, __value: _T, __start: SupportsIndex = ..., __stop: SupportsIndex = ...) -> int:
        return super().index(__value, __start=__start, __stop=__stop)

    def count(self, __value: _T) -> int:
        return super().count(__value)
