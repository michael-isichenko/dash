import pandas as pd
import numpy as np


def f4(q, p, s, v):
    return np.sqrt(q)*v + p*s*v

xx = {
    'q' : np.linspace(0, 2, 100),
    'p' : np.linspace(0, 0.5, 100),
    's' : np.linspace(0, 0.01, 100),
    'v' : np.linspace(0, 0.05, 100),
}


def f42(vv: dict[str]->float):
    assert len(vv) == 3
    x = None
    for key in xx.keys:
        if key not in vv:
            assert x is None
            x = key
    df = pd.DataFrame()
    df[x] = xx[x]
    if x == 'q':
        df['y'] = f4(xx[x], vv['p'], vv['s'], vv['v'])
    elif x == 'p':
        df['y'] = f4(vv['q'], xx[x], vv['s'], vv['v'])
    elif x == 's':
        df['y'] = f4(vv['q'], vv['p'], xx[x], vv['v'])
    else: # x == 'v'

    if x1 == 'q':
        if x2 == p:
            return 