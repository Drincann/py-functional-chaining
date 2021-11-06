from abc import abstractmethod


class BaseType:
    @classmethod
    @abstractmethod
    def pack(cls, _):
        raise NotImplementedError()
