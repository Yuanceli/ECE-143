def is_string_integer(instring):
    '''
    returns True if given character represents a valid integer in base 10.

    :return:bool
    '''
    assert isinstance(instring, str), 'Input is not a string.'
    assert len(instring)==1, 'Input is not a single character.'
    return ('0' <= instring <='9')
