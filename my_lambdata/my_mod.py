def date_cols(df, date_col):
    '''
    Takes a dataframe and a column that is a date and returns
    three columns for Year, Month, and Day
    '''
    import pandas as pd

    df[date_col] = pd.to_datetime(df[date_col], infer_datetime_format=True)
    df['Year'] = df[date_col].dt.year
    df['Month'] = df[date_col].dt.month
    df['Day'] = df[date_col].dt.day