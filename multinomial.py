import random
def multinomial_sample(n,p,k=1):  
    '''                                                                 
    Return samples from a multinomial distribution.                     
                                                                       
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''                         
    assert isinstance(n, int) and n > 0
    assert isinstance(p, list) and sum(p) == 1
    assert isinstance(k, int) and k > 0
    outlist = []
    for trial in range(k):
        sample = []
        outindex = random.choices([index for index, value in enumerate(p)], weights = p, k = n)
        for s in range(len(p)):
            sample.append(outindex.count(s))
        outlist.append(sample)
    return outlist
