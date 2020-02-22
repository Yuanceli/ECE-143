def fibonacci(n):
    '''
    produce a fibonacci sequence of n numbers
    :input: n
    :type: int
    '''
    assert isinstance(n, int)
    assert n>=1
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a+b
