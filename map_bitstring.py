def map_bitstring(inlist):
    '''
    takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0
    if the number of 0s in the bitstring strictly exceeds the number of 1s.
    Otherwise, map that bitstring to 1.
    '''
    assert isinstance(inlist,list) and len(inlist) > 0
    y = set(inlist)
    d = dict()
    for i in y:
        assert isinstance(i, str)
        if i.count('0') > i.count('1'):
            d[i] = 0
        else:
            d[i] = 1
    return d
