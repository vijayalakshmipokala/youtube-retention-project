from textblob import TextBlob
import pandas as pd

def add_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    def get_sentiment(text):
        if pd.isna(text):
            return 0
        return TextBlob(str(text)).sentiment.polarity

    df["sentiment_score"] = df["description"].apply(get_sentiment)
    return df