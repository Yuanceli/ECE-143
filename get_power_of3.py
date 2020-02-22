def get_power_of3(x):
    '''
    using the set {1,3,9,27} and the addition and subtraction operations,
    construct any integer between 1 and 40 without re-using elements.

    :return:a 4-element list of the decomposition
    '''
    assert isinstance(x, int), 'Input should be an nonnegative integer'
    assert 1 <= x <= 40, 'Input should be between 0 and 40'
    a = [0,0,0,0]
    for i in range(4):
        a[i] += x % 3
        x = x // 3
        if a[i] == 2:
            a[i] = -1
            a[i+1] += 1
        elif a[i] == 3:
            a[i] = 0
            a[i+1] += 1
    return a
