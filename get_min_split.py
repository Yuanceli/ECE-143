#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools as iter
import numpy as np
def get_min_split(seq):
    '''
    Given an array of unique positive integers, divide the array into two subsets such that
    the absolute difference between the respective sums of the subsets is as small as possible.
    '''
    assert isinstance(seq, list) or (isinstance(seq, np.ndarray) and seq.ndim == 1)
    assert (isinstance(i, int) for i in seq)
    assert len(seq) == len(set(seq))
    half = sum(seq) / 2
    combine = []
    subtract = []
    outlist = []
    for r in range(1, len(seq)+1):
        mid = list(iter.combinations(seq, r))
        for miditem in mid:
            combine.append(miditem)
            subtract.append(abs(sum(miditem)-half))
    length = len(seq)
    for i, x in enumerate(combine):
        if subtract[i] == min(subtract):
            if length > len(x):
                length = len(x)
    for i, x in enumerate(combine):
        if subtract[i] == min(subtract) and len(x) == length:
            outlist.append( ( sorted(list(x)),sorted(list(set(seq)-set(x) )) ) )
    return outlist

