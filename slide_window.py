def slide_window(x,width,increment):
    '''
    The function should take the window width and the window increment as inputs
    and should produce a sequence of overlapping lists from the input list.
    '''
    assert isinstance(x, list) and len(x) >= 1
    assert isinstance(width, int) and width >= 1
    assert isinstance(increment, int) and increment >=1
    assert len(x) >= width
    t = []
    count = 0
    for num in range((len(x)-width) // increment + 1):
        item = []
        for i in range(width):
            item.append(x[count+i])
        count += increment
        t.append(item)
    return t
