import numpy as np
import random as rd
def gen_rand_slash(m=6,n=6,direction='back'):
    '''
    produce a uniformly random forward or backslashed image
    '''
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert m > 0 and n > 0
    assert direction == 'back' or direction == 'forward'
    length = rd.randint(2,min(m,n))
    t = np.zeros((m,n))
    if direction == 'back':
        m_start = rd.randint(0,m-2)
        n_start = rd.randint(0,n-2)
        for i in range(length):
            if m_start >= m or n_start >= n:
                break
            else:
                t[m_start][n_start] = 1
                m_start += 1
                n_start += 1
    else:
        m_start = rd.randint(1,m-1)
        n_start = rd.randint(0,n-2)
        for i in range(length):
            if m_start < 0 or n_start >= n:
                break
            else:
                t[m_start][n_start] = 1
                m_start -= 1
                n_start += 1
    return t
