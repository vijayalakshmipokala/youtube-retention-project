import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def normalize_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize numerical features to same scale
    """
    scaler = MinMaxScaler()

    df[['views_n', 'engagement_n', 'sentiment_n']] = scaler.fit_transform(
        df[['views', 'engagement_rate', 'sentiment_score']]
    )

    return df


def add_time_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assign score based on peak engagement hours
    """
    df['time_score'] = df['hour'].apply(
        lambda x: 1 if 18 <= x <= 21 else 0.5
    )
    return df


def calculate_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Final weighted score calculation
    """

    df['score'] = (
        0.35 * df['views_n'] +
        0.35 * df['engagement_n'] +
        0.2 * df['sentiment_n'] +
        0.1 * df['time_score']
    )

    return df


def scoring_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full scoring pipeline
    """
    df = normalize_features(df)
    df = add_time_score(df)
    df = calculate_score(df)

    return df