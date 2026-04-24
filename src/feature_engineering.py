import pandas as pd


def feature_engineering_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create features for retention analysis
    """

    # Engagement features
    df['engagement_rate'] = (df['likes'] + df['comment_count']) / df['views']
    df['like_ratio'] = df['likes'] / df['views']
    df['comment_ratio'] = df['comment_count'] / df['views']

    # Time features
    df['publish_time'] = pd.to_datetime(df['publish_time'])
    df['day'] = df['publish_time'].dt.day_name()
    df['hour'] = df['publish_time'].dt.hour

    # Controversy score
    df['controversy'] = df['dislikes'] / df['views']

    # Simple sentiment proxy (placeholder if not already computed)
    if 'sentiment_score' not in df.columns:
        df['sentiment_score'] = 0.0

    return df