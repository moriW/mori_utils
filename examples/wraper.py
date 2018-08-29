#!/usr/bin/env python
"""
@author: Mori
@contact: moridisa@moridisa.com
@file: wraper
@time: 2018/8/29 11:34 AM
@desc: Code By Mori
"""

from mori_utils import *


# cache with func and module name
@m_wrap()
def foo() -> int:
    print('execute foo')
    return sum(range(10))


# cache with func and module name and args
@m_wrap(cache_args=[0])
def foo_2(x: int) -> int:
    print('execute foo 2')
    return sum(range(x))


# cache with func and module name and kw args
@m_wrap(cache_kwargs=['x'])
def foo_3(x: int = 5) -> int:
    print('execute foo 3')
    return sum(range(x))


# cache with func and module name and args / kwargs automatic
@m_wrap()
def foo_4(x: int = 2) -> int:
    print('execute foo 4')
    return sum(range(x))


# cache file prefix and suffix
@m_wrap(prefix='cache', suffix='for test')
def foo_5():
    print('execute foo 5')
    return 5


# cache file expire time / for day
@m_wrap(cache_expire=5)
def foo_6():
    print('execute foo 6')
    return 12345
