def get_trapped_water(seq):
    '''
    :param seq: input, list
    :return: int
    '''
    assert isinstance(seq,list)
    n=len(seq)
    # left[i] contains height of tallest bar to the left of i th bar including itself
    left_bar = seq[:]
    right_bar = seq[:]
    trap_water = 0
    for i in range(1, n):
        left_bar[i] = max(left_bar[i - 1], seq[i])    
    for i in range(n-2, -1, -1):
        right_bar[i] = max(right_bar[i + 1], seq[i])
    for i in range(1, n):
        trap_water += min(left_bar[i], right_bar[i]) - seq[i]
    return trap_water
