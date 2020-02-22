def compute_sum_to_n(n):
    '''
    computes the sum of all non-negative integers up to
    and including a specified value, n.

    :return:int
    '''
    assert isinstance(n,int)
    assert n>=0
    a = [];
    for i in range(n+1):
        a.append(i)
    s = sum(a)
    return s
