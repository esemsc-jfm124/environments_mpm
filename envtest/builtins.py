import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import datetime as dt


__all__ = ['rand_array','smooth_image', 'my_mat_solve','date_time']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def date_time(a=1990,b=3,c=12):
    date_of_birth = dt.datetime(a, b, c)
    print(dt.datetime.today() - date_of_birth)


