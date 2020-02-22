def write_columns(data,fname):
    '''
    write the following formula to three columns to a comma-separated file:
    data_value, data_value**2, (data_value+data_value**2)/3
    '''
    assert isinstance(data, list)
    assert isinstance(fname, str)
    f = open(fname, 'w')
    for i in range(len(data)):
        assert isinstance(data[i], int) or isinstance(data[i], float)
        a = data[i]
        b = data[i]**2
        c = (a+b) / 3
        print('%.2f, %.2f, %.2f' % (a, b, c))
        f.write('%.2f, %.2f, %.2f\n' % (a, b, c))
