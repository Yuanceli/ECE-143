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
