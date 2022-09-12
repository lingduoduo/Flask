# -*- coding: utf-8 -*-
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print(' class decorator running ')
        self._func(*args, **kwargs)
        print(' class decorator ending ')


@Foo
def bar(strs):
    print(strs)


bar("i am bar")
