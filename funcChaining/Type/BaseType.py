from abc import abstractmethod


class BaseType:
    @abstractmethod
    def pack(cls, _):
        pass
