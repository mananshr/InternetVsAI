import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Analysis: growth of AI")

st.header("Perdictive analysis")
df = pd.read_csv("data/ai/Global Artificial Intelligence Market .csv")

st.area_chart(df, x="Year", y="Overall", y_label="Global AI market, 2017-2030 (US$M)")

df_extra = pd.read_csv("data/ai/The Rise Of Artificial Intellegence2.csv")

df_extra_market = df_extra[["Year", "AI Software Revenue(in Billions)",
                                     "Global AI Market Value(in Billions)"]]
df_extra_market = df_extra_market.rename(columns={"AI Software Revenue(in Billions)":"AI Software Revenue", "Global AI Market Value(in Billions)":"Global AI Market Value"})

st.line_chart(df_extra_market, x="Year", y=["AI Software Revenue",
                                     "Global AI Market Value"],
                                     y_label="In Billions")

# st.line_chart(df_extra, x="Year", y="AI Adoption (%)")
fig = px.line(df_extra, x="Year", y="AI Adoption (%)")
st.plotly_chart(fig)

# df_extra_jobs = df_extra[["Year","Estimated Jobs Eliminated by AI (millions)",
#                                      "Estimated New Jobs Created by AI (millions)"]]
# df_extra_jobs

# # st.line_chart(df_extra_jobs, x="Year", y_label="Percent")
# fig = px.line(df_extra_jobs, x="Year", y="Estimated Jobs Eliminated by AI (millions)")
# fig.add_scatter(x=df_extra_jobs['Year'], y=df_extra_jobs['Estimated New Jobs Created by AI (millions)'])
# st.plotly_chart(fig)


# st.line_chart(df_extra, x="Year", y=["AI Software Revenue(in Billions)",
#                                      "Global AI Market Value(in Billions)",
#                                      "AI Adoption (%)",
#                                      "Organizations Using AI,Organizations Planning to Implement AI,Global Expectation for AI Adoption (%)",
#                                      "Estimated Jobs Eliminated by AI (millions)",
#                                      "Estimated New Jobs Created by AI (millions)",
#                                      "Net Job Loss in the US",
#                                      "Organizations Believing AI Provides Competitive Edge",
#                                      "Companies Prioritizing AI in Strategy,Estimated Revenue Increase from AI (trillions USD)",
#                                      "Marketers Believing AI Improves Email Revenue,Expected Increase in Employee Productivity Due to AI (%)",
#                                      "Americans Using Voice Assistants (%),Digital Voice Assistants (billions of devices)",
#                                      "Medical Professionals Using AI for Diagnosis",
#                                      "AI Contribution to Healthcare(in Billions)",
#                                      "Jobs at High Risk of Automation - Transportation & Storage (%)",
#                                      "Jobs at High Risk of Automation - Wholesale & Retail Trade",
#                                      "Jobs at High Risk of Automation - Manufacturing"],
#                                      y_label="In Billions")