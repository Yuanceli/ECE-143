def get_average_word_length(words):
    '''
    compute the average length of words
    '''
    assert isinstance(words, list)
    count = 0
    for i in words:
        assert isinstance(i, str)
        count += len(i)
    return count/len(words)

def get_longest_word(words):
    '''
    longest word
    '''
    assert isinstance(words, list)
    a = words[0]
    for i in words:
        assert isinstance(i, str)
        if len(i) > len(a):
            a = i
    return a

def get_longest_words_startswith(words,start):
    '''
    longest word starts with a single letter
    '''
    assert isinstance(words, list)
    assert isinstance(start, str)
    assert 'a' <= start <= 'z' or 'A' <= start <= 'Z'
    b = start
    for i in words:
        assert isinstance(i, str)
        if i[0] == start:
            if len(i) >= len(b):
                b = i
    return b

def get_most_common_start(words):
    '''
    most common starting letter
    '''
    assert isinstance(words, list)
    count = dict()
    for i in words:
        assert isinstance(i, str)
        if i[0] not in count.keys():
            count[i[0]] = 1
        else:
            count[i[0]] += 1
    c = max(count, key = count.get)
    return c

def get_most_common_end(words):
    '''
    most common end letter
    '''
    assert isinstance(words, list)
    assert all(isinstance(i, str) for i in words)
    count = dict()
    for i in words:
        if i[-1] not in count.keys():
            count[i[-1]] = 1
        else:
            count[i[-1]] += 1
    d = max(count, key = count.get)
    return d
