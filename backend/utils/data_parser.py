import pandas as pd

def normalize_dataframe(data):
    """
    Normalize the given data into a Pandas DataFrame.

    Args:
        data (dict): The raw data to be normalized.

    Returns:
        pd.DataFrame: The normalized DataFrame.
    """
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index = pd.to_datetime(df.index)
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.astype(float)
    return df
