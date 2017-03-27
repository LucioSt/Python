# -*- coding: utf-8 -*-
# 
# Calcula o tempo de execução da função decorada
# 
# Uso:
# 
# @clock
# def func_teste(x):
#     print('x')
# 
# ----------------------------------------
# 0.12813115s - snooze(0.123) -> None
# ----------------------------------------

import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('-' * 40)
        print('Time used: %0.8fs - %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        print('-' * 40)
        return result
    return clocked
