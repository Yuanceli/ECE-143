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

def fix_categorical(x):
    '''
    :param x: input, dataframe
    :return: dataframe
    '''
    assert isinstance(x, pd.DataFrame)
    cat = pd.api.types.CategoricalDtype(categories=['Sep-2017', 'Jan-2018', 'Feb-2018', 'Mar-2018','Apr-2018','Sep-2018','Oct-2018','Jan-2019'],ordered=True)
    x['month-yr'] = x['month-yr'].astype(cat)
    return x
