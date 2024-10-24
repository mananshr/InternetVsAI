import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI plays chess")

df = pd.read_csv("data/ai/computer-chess-ability.csv")

fig = px.line(df, x="Year", y="Elo rating", title="Elo rating of AI over the years")
st.plotly_chart(fig)