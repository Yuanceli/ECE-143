import pandas as pd
def add_month_yr(x):
    '''
    :param x: input, dataframe
    :return: dataframe
    '''
    assert isinstance(x, pd.DataFrame)
    month = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
             '5': 'May', '6': 'Jun', '7': 'Jul', '8': 'Aug',
             '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    outlist = []
    for i in x['Timestamp'].str.split('/| '):
        outlist.append(month[i[0]] + "-" + i[2])
    z = x.iloc[:]
    z['month-yr'] = outlist
    return z

def count_month_yr(x):
    '''
    :param x: input, dataframe
    :return: dataframe
    '''
    # x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index() 
    assert isinstance(x, pd.DataFrame)
    inframe = add_month_yr(x)
    midframe = inframe.loc[:, ['Timestamp','month-yr']]
    outframe = midframe.groupby(['month-yr']).count() 
    return outframe
