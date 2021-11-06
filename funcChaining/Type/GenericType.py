from .BaseType import BaseType


class GenericType(BaseType):
    @staticmethod
    def packStrict(obj):
        from .List import List
        if isinstance(obj, list) or isinstance(obj, List):
            return List.pack(obj)
        else:
            raise TypeError(
                'Factory.packStrict: value must be one of (list, )')

    @staticmethod
    def pack(obj):
        from .List import List
        if isinstance(obj, list) or isinstance(obj, List):
            return List.pack(obj)
        else:
            return obj
