def write_chunks_of_five(words,fname):
    '''
    create a new file that consists of each consecutive non-overlapping sequence
    of five lines merged into one line.
    '''
    assert isinstance(words, list)
    assert isinstance(fname, str)
    f = open(fname,'w')
    for i, x in enumerate(words):
        print(x,end=' ',file=f)
        if i % 5 == 4:
            print('\n',end='',file=f)
