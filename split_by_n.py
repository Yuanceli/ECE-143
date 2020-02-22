import os
def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    assert isinstance(fname, str) and isinstance(n, int)
    assert n > 0
    f = open(fname, 'r')
    b = f.readlines()
    size = os.path.getsize(fname)
    ave = size / n
    split = []
    start = 0
    piece = 0
    for i,x in enumerate(b):
        if len(split) >= n-1:
            split.append(b[start:])
            break
        elif ave - piece >= len(x):
            piece += len(x)
        else:
            split.append(b[start:i])
            start = i
            piece = len(x)
    for num in range(len(split)):
        w = open(('{}{}{:0>3d}{}'.format(fname, '_', num, '.txt')), 'wt')
        w.writelines(split[num])
    return split
