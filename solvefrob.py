import numpy as np
def solvefrob(coefs,b):
    '''
    a_1 x_1 +... + a_n x_n = b
    '''
    assert isinstance(coefs, list)
    assert isinstance(b, int)
    assert (isinstance(i, int) for i in coefs)
    assert (i > 0 for i in coefs)
    assert b > 0
    x = []
    for i,item in enumerate(coefs):
        x.append(np.arange(b // item + 1) * np.array([item]))
    sum_ax = 0
    for i in range(len(x)):
        list1=[]
        for j,item in enumerate(coefs):
            if j == i:
                list1.append(b // item + 1)
            else:
                list1.append(1)
        shape = tuple(list1)
        ax = x[i].reshape(shape)
        sum_ax = sum_ax + ax

    solution = [tuple(i) for i in np.array(np.where(sum_ax==b)).T]
    return solution
