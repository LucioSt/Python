#!/usr/bin/env python

def verbose(func):
    """
    :param func: Simple template for decorator, without parameters
    :return:
    """
    def wrapper(*args, **kwargs):
        print("After of:", func.__name__)
        result = func(*args, **kwargs)
        print("Before of:",func.__name__)
        return result
    wrapper.__doc__  = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper


def param_dec(option):
    """
    :param option: template for parameterized decorator
    :return: function decorated
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            # use option parameter here
            # before
            result = function(*args, **kwargs)
            # after
            return result
        wrapper.__doc__ = function.__doc__
        wrapper.__name__ = function.__name__
        return wrapper
    return decorator




@verbose
def something(x,y):
    print("Sum:",x+y)


@param_dec(5)
def something__2__(x,y):
    print("Sum:",x+y)



something__2__(1,2)

# Resultado:
# After of: something
# Sum: 3
# Before of: something
