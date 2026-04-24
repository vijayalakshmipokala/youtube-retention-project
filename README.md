#  YouTube Video Retention & Ranking System

An end-to-end data science project that analyzes YouTube trending videos and builds a ranking system to predict high-engagement content using feature engineering, scoring models, evaluation metrics, and an interactive dashboard.

---

## Project Objective

The goal of this project is to:
- Analyze YouTube trending video dataset
- Engineer meaningful engagement-based features
- Build a scoring system to rank videos
- Evaluate model performance against baseline methods
- Visualize insights using an interactive Streamlit dashboard

---

##  Project Structure

youtube-retention-project/
│
├── data/
│   ├── raw/
│   │   └── USvideos.csv
│   │
│   └── processed/
│       ├── cleaned_videos.csv
│       ├── featured_videos.csv
│       └── scored_videos.csv
│
├── notebooks/
│   ├── 01_problem_definiton.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_recommendation_engine.ipynb
│   └── 05_eda.ipynb
|   |__06_model_evaluation.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── scoring_model.py
│   ├── recommend.py
│   └── sentiment_analysis.py
│
├── app/
│   └── streamlit_app.py
│
├── outputs/
│   ├── scored_videos.csv
│   └── top_recommendations.csv
│
├── reports/
│   ├── figures/
│   │   ├── model_comparison.png
│   │   ├── top_k_rankings.png
│   │   └── score_distribution.png
│   │
│   └── insights.md
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore

---

##  Workflow

### 1. Data Preprocessing
- Loaded raw YouTube trending dataset
- Cleaned missing and inconsistent data

### 2. Feature Engineering
Created meaningful features:
- Engagement rate
- Like ratio
- Comment ratio
- Time-based features (hour, day)
- Sentiment score (optional)

### 3. Scoring Model
Built a weighted scoring system to rank videos based on engagement signals.

### 4. Recommendation System
Generated top-ranked videos based on computed scores.

### 5. Evaluation
Compared model performance using:
- Precision@K metric
- Baseline comparison (views-based ranking)

### 6. Visualization
Created insights using:
- Matplotlib plots
- Streamlit dashboard

---

##  Key Results

- Feature-engineered model outperforms simple view-based ranking
- Engagement features strongly predict video performance
- Ranking system provides better and stable recommendations

---

##  Dashboard Features

Built using Streamlit:
- Model vs baseline comparison
- Top-K video ranking viewer
- Interactive filters
- Performance insights

---

##  Reports & Figures

All visualizations are stored in: reports/figures/

Includes:
- Model comparison chart
- Top-K ranked videos
- Score distribution plot

---

##  Key Insights

- Engagement metrics outperform raw views in ranking quality
- Channel behavior strongly influences video performance
- Composite scoring improves recommendation accuracy

---

##  Limitations

- No real-time YouTube API integration
- No deep learning model used
- Sentiment analysis is basic (optional improvement)

---

##  Future Improvements

- Integrate YouTube Data API for live data
- Replace scoring system with ML models (XGBoost / LightGBM)
- Deploy Streamlit dashboard online
- Add personalization-based recommendations

---

##  Tech Stack

- Python
- Pandas, NumPy
- Matplotlib
- Streamlit
- Feature Engineering
- Ranking Systems

---

##  How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run pipeline
python main.py

# Launch dashboard
streamlit run app/streamlit_app.py