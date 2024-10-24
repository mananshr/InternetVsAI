import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/ai/The Rise Of Artificial Intellegence2.csv")

st.title("Jobs under AI")

# st.line_chart(df, x="Year", y={"Jobs at High Risk of Automation - Transportation & Storage (%)",
#                                       "Jobs at High Risk of Automation - Wholesale & Retail Trade",
#                                       "Jobs at High Risk of Automation - Manufacturing"})

df = df.rename(columns={"Jobs at High Risk of Automation - Transportation & Storage (%)": "Transportation & Storage"})
df = df.rename(columns={"Jobs at High Risk of Automation - Wholesale & Retail Trade": "Wholesale & Retail Trade"})
df = df.rename(columns={"Jobs at High Risk of Automation - Manufacturing": "Manufacturing"})

fig = px.line(df, x="Year", y=["Transportation & Storage", "Wholesale & Retail Trade", "Manufacturing"], title="Jobs at high risk of automation.")

# fig = px.line(df, x="Year", y="Transportation & Storage", hover_name="Transportation & Storage", title="Jobs at high risk of automation.")

# fig.add_scatter(x=df['Year'], y=df['Jobs at High Risk of Automation - Wholesale & Retail Trade'], hovertext="Wholesale & Retail Trade")

# fig.update_traces({'name': 'Wholesale & Retail Trade'})

fig.update_layout(yaxis_title="Percentage")
st.plotly_chart(fig)