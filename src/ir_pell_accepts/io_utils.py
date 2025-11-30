#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pathlib import Path
from typing import Union

import pandas as pd


def infer_and_read_file(file: Union[str, Path]) -> pd.DataFrame:
    """
    Read a file into a pandas DataFrame, inferring its extension.

    Supported file types:
        - .xlsx : Excel workbook
        - .csv  : Comma-separated values
        - .txt  : Tab-delimited text file

    Parameters
    ----------
    file : str or pathlib.Path : Path to the input file.

    Returns
    -------
    pandas.DataFrame : The loaded data with all columns converted to strings.

    Raises
    ------
    FileNotFoundError
        If the provided file path does not exist.
    ValueError
        If the file extension is not one of the supported types.
    """

    allowed = {'.xlsx', '.csv', '.txt'}

    path = Path(file)

    if not path.exists():
        raise FileNotFoundError(f'Input file does not exist: {path}')

    ext = path.suffix.lower()

    if ext == '.xlsx':
        out = pd.read_excel(path, dtype=str)
    elif ext == '.csv':
        out = pd.read_csv(path, dtype=str)
    elif ext == '.txt':
        out = pd.read_csv(path, dtype=str, sep='\t')
    else:
        raise ValueError(f'Unsupported file type: {ext}. Allowed values: {allowed}')

    return out

