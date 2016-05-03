""" The first file I am creating """

# Put the directory where this library is, in your PYTHONPATH
#  or run ipython from this directory. (to know the path a directory)
#  run "pwd"

import numpy as np


def sinx(x,a=1):
    """ returns the sin of x time a.
                (pip8)
    Parameters:
    x: value in radian (could be an array)
    a: the amplitude of the returns sin (a float/int).
       This amplitude have to be positive
    """
    if a <0: 
        return [np.NaN]*len(x)
    
    return np.sin(x)*a


def printer(x):
    """ only prints x """
    print(x)




def get_dice(size=None):
    """ this returns a value between 1 and 6"""
    
    return np.random.randint(1,7,size=size)

