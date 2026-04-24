import pandas as pd


def recommend_videos(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """
    Recommend top N videos based on score
    """

    # Ensure score exists
    if "score" not in df.columns:
        raise ValueError("Missing 'score' column in dataframe")

    # Remove duplicates safely inside function
    df_unique = df.drop_duplicates(subset=['video_id', 'category_id'], keep='first')

    # Sort and pick top N
    recommended = df_unique.sort_values(by='score', ascending=False).head(top_n)

    return recommended[['title', 'channel_title', 'score']]


def save_recommendations(df: pd.DataFrame, path: str = "outputs/top_recommendations.csv"):
    """
    Save recommendations to CSV
    """
    df.to_csv(path, index=False)
    print(f"Saved recommendations to {path}")