import random as rd
import string
def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 

    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message, str)
    assert isinstance(fname, str)
    f = open(fname, 'r')
    book = f.readlines()
    words = message.split()
    dictionary = {i:[] for i in set(words)}
    for l, line in enumerate(book):
        reline = line.lower()
        reline.translate(reline.maketrans('', '', string.punctuation))
        for w, word in enumerate(reline.split()):
            if word in dictionary.keys():
                dictionary[word].append((l+1, w+1))
    assert (len(dictionary[j]) >= words.count(j) for j in words)
    outlist = []
    for index, item in enumerate(words):
        while 1:
            r = rd.choice(dictionary[item])
            if r not in outlist:
                outlist.append(r)
                break
            else:
                continue
    return outlist
    
def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message. 

    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert isinstance(inlist, list)
    assert (isinstance(i, tuple) for i in inlist)
    assert isinstance(fname, str)
    f = open(fname, 'r')
    book = f.readlines()
    message = []
    for i in inlist:
        line = book[i[0]-1]
        line = line.lower()
        line.translate(line.maketrans('', '', string.punctuation))
        word = line.split()
        message.append(word[i[1]-1])
    return ' '.join(message)
