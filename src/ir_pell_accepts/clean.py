import pandas as pd

def remove_leading_zeros(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Remove leading zeros from a given column of a dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
    column : str
        name of column
    
    Returns
    -------
    pandas.DataFrame
        df is returned with df[column] free of leading zeros

    Raises
    ------
    ValueError
        If column is not present in df.
    """
    if not column in df.columns:
        raise ValueError(f"{column} column is not present in the dataframe.")
    
    df = df.copy()
    df['ID'] = df['ID'].astype(str).str.lstrip('0')

    return df
