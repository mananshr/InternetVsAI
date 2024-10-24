import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Growth of Broadband")

df = pd.read_csv("data/broadband-penetration-by-country.csv")
df = df.rename(columns={"Fixed broadband subscriptions (per 100 people)": "Fixed broadband subscriptions"})
df

df_world = df.loc[df['Entity']=='World']
df_world

fig = px.area(df_world, x="Year", y="Fixed broadband subscriptions", title="Fixed broadband subscriptions (per 100 people)")
st.plotly_chart(fig)