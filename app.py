import streamlit as st

internet_coverage = st.Page("Internet/Coverage.py")
internet_broadband = st.Page("Internet/Broadband.py")

ai_growth = st.Page("AI/Growth.py")
ai_jobs = st.Page("AI/Jobs.py")

pg = st.navigation(
    {
        "Internet": [internet_coverage, internet_broadband],
        "AI": [ai_growth, ai_jobs],
        "Comparision": []
    }
)
pg.run()