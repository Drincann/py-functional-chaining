import functools


class List(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def map(self, func):
        return List(map(func, self))

    def filter(self, func):
        return List(filter(func, self))

    def reduce(self, func, initial=None):
        return functools.reduce(func, self, initial)
