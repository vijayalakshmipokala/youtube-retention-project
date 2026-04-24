import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna(subset=['description'])
    df = df[df['video_error_or_removed'] == False]
    return df


def convert_datatypes(df: pd.DataFrame) -> pd.DataFrame:
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df = df.dropna(subset=['publish_time'])
    return df


def remove_outliers(df: pd.DataFrame) -> pd.DataFrame:
    upper_limit = df['views'].quantile(0.99)
    df = df[df['views'] < upper_limit]
    return df


def preprocess_data(file_path: str) -> pd.DataFrame:
    df = load_data(file_path)
    df = basic_cleaning(df)
    df = convert_datatypes(df)
    df = remove_outliers(df)
    return df