import pandas as pd
import numpy as np


def f4(q, p, s, v):
    return np.sqrt(q)*v + p*s*v

qq = np.linspace(0, 2, 100)
pp = np.linspace(0, 0.5, 100)
ss = np.linspace(0, 0.01, 100) 
vv = np.linspace(0, 0.05, 100)


def f42(x1, v1, x2, v2):
    if x1 == 'q':
        if x2 == p:
            return 