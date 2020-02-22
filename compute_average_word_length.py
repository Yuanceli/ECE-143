def compute_average_word_length(instring,unique=False):
    '''
    compute the average length of the words in the input string
    If the unique option is True, then exclude duplicated words.

    type(instring) is str
    type(unique) is bool
    '''
    assert isinstance(instring, str)
    assert len(instring)>0
    assert isinstance(unique, bool)
    temp = instring.split()
    words = []
    totallength = 0
    for item in temp:
        word = ''
        for j in item:
            if '0' <= j <= '9' or 'a' <= j <= 'z' or 'A' <= j <= 'Z':
                word = word + j
        if len(word) > 0:
            words.append(word)
    if unique:
        words = set(words)
    if len(words) == 0:
        return 0.0
    for x in words:
        totallength += len(x)
    return totallength/len(words)
