import streamlit as st
import pandas as pd

st.title("Growth of Broadband")

df = pd.read_csv("data/mobile-cellular-subscriptions-per-100-people.csv")
df = df.rename(columns={"Mobile cellular subscriptions (per 100 people)": "Mobile cellular subscriptions"})
df

df_world = df.loc[df['Entity']=='World']
df_world

st.line_chart(df_world, x="Year", y="Mobile cellular subscriptions", title="Mobile cellular subscriptions (per 100 people)")