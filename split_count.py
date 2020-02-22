import pandas as pd
def split_count(x):
    '''
    :param x: input, series
    :return: dataframe
    '''
    assert isinstance(x, pd.Series)
    item = []
    for i in x.str.split(', '):
        for j in i:
            item.append(j)
    itemseries = pd.Series(item)
    count = itemseries.value_counts(ascending = True)
    outframe = pd.DataFrame({'count': count})
    return outframe
