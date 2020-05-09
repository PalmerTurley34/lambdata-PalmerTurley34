def list_to_col(df, lst, col_name):
    '''
    takes a list and a name for that list. changes the list to a series,
    and adds that series to a given dataframe
    '''

    import pandas as pd
    series = pd.Series(lst)
    df[col_name] = series