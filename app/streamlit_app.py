import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="YouTube Retention Dashboard", layout="wide")

st.title("YouTube Retention Model Dashboard")

# Load data
DATA_PATH = "outputs/scored_videos.csv"

if not os.path.exists(DATA_PATH):
    st.error("scored_videos.csv not found. Run main.py first.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# Safety check
if "score" not in df.columns:
    st.error("Score column missing. Check scoring pipeline.")
    st.stop()

# Create true engagement
df["true_score"] = df["likes"] + df["comment_count"]

# Sidebar controls
st.sidebar.header("Controls")

k = st.sidebar.slider("Top K Videos", 5, 50, 10)

model_choice = st.sidebar.selectbox(
    "Choose Ranking Model",
    ["Score-Based Model", "Views Baseline"]
)

# Select ranking column
if model_choice == "Score-Based Model":
    rank_col = "score"
else:
    rank_col = "views"

# Sort data
top_k = df.sort_values(rank_col, ascending=False).head(k)

# Metrics
st.subheader("Model Performance (Top-K Avg Engagement)")

model_score = top_k["true_score"].mean()

baseline_score = df.sort_values("views", ascending=False).head(k)["true_score"].mean()

col1, col2 = st.columns(2)

with col1:
    st.metric("Selected Model Score", round(model_score, 3))

with col2:
    st.metric("Views Baseline Score", round(baseline_score, 3))

# Table
st.subheader("Top Ranked Videos")

st.dataframe(top_k[["title", "channel_title", "views", "likes", "comment_count", "score"]])

# Simple insight
st.subheader("Insight")

if model_score > baseline_score:
    st.success("Your model performs better than views-based ranking 🚀")
else:
    st.warning("Views baseline is performing better — improve feature weights.")