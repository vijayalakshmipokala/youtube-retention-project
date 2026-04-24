import sys
import os
import pandas as pd

sys.path.append("src")

from preprocessing import preprocess_data
from feature_engineering import feature_engineering_pipeline
from scoring_model import scoring_pipeline
from recommend import recommend_videos, save_recommendations
from sentiment_analysis import add_sentiment


def main():
    print("Starting YouTube Retention Pipeline...")

    # Step 1: Load + Clean
    df = preprocess_data("data/raw/USvideos.csv")
    print("Data cleaned!!")

    print("after preprocessing shape:", df.shape)
    print(df.head())

    # Step 2: Feature Engineering
    df = feature_engineering_pipeline(df)
    print("Features created!!")

    # Step 3: sentiment analysis
    df = feature_engineering_pipeline(df)
    df = add_sentiment(df)
    print("Sentiment analysis added!!")

    # Step 4: Scoring
    df = scoring_pipeline(df)
    print("Scoring applied!!")

    print("after scoring shape:", df.shape)
    print(df.columns)

    # Step 5: Create recommendations
    top_videos = recommend_videos(df, top_n=10)
    print("Recommendations generated!!")

    # Step 6: Create outputs folder if not exists
    os.makedirs("outputs", exist_ok=True)

    # Step 7: SAVE FULL SCORED DATASET (IMPORTANT)
    df.to_csv("outputs/scored_videos.csv", index=False)
    print("Full scored dataset saved to outputs/scored_videos.csv")

    # Step 8: SAVE TOP RECOMMENDATIONS
    save_recommendations(top_videos, "outputs/top_recommendations.csv")
    print("Top recommendations saved to outputs/top_recommendations.csv")

    # Step 9: Print results
    print("\nTop Recommendations:")
    print(top_videos.head(10))

    print(os.getcwd())


if __name__ == "__main__":
    main()