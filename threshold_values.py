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

def get_sample(nbits=3, prob=None, n=1):
    '''
    return a list n of random samples from a finite probability mass function
    defined by a dictionary with keys defined by a specified number of bits
    '''
    assert isinstance(nbits,int) and isinstance(n,int)
    assert nbits > 0 and n > 0
    assert isinstance(prob,dict)
    assert (0 <= x <= 1 for x in prob.values())
    assert sum(list(prob.values())) == 1
    assert (len(y) == nbits for y in prob.keys())
    assert len(prob) == 2**nbits
    import random
    order = random.sample(list(prob),n)
    return order

def gather_values(inlist):
    '''
    generate n samples and tally the number of times an existing key is repeated
    '''
    assert isinstance(inlist, list)
    m = map_bitstring(inlist)
    d = dict()
    for i in set(inlist):
        assert isinstance(i, str)
        v = []
        for num in range(inlist.count(i)):
            v.append(m[i])
        d[i] = v
    return d

def threshold_values(seq,threshold=1):
    '''
    threshold those values based upon their frequency and value
    '''
    assert isinstance(seq, list)
    assert (isinstance(x, str) for x in seq)
    assert isinstance(threshold, int)
    assert threshold <= len(set(seq))
    g = gather_values(seq)
    count = dict()
    for i in g:
        count[i] = sum(g[i])
    findT = sorted(count.values(), reverse = True)
    T = findT[threshold-1]
    order = dict(sorted(count.items(), key = lambda x:x[0]))
    final = dict()
    for j in order.keys():
        if order[j] > T:
            final[j] = 1
        else:
            final[j] = 0
    k = threshold - sum(final.values())
    for j in order.keys():
        if k > 0:
            if count[j] == T:
                final[j] = 1
                k -= 1
        else:
            break
    return final
