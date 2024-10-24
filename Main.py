import streamlit as st

internet_coverage = st.Page("Internet/Coverage.py")
internet_broadband = st.Page("Internet/Broadband.py")
internet_mobile_phone = st.Page("Internet/Mobile_Phone.py")

ai_growth = st.Page("AI/Growth.py")
ai_jobs = st.Page("AI/Jobs.py")
ai_chess = st.Page("AI/AI_Plays_Chess.py")

pg = st.navigation(
    {
        "Internet": [internet_coverage, internet_broadband, internet_mobile_phone],
        "AI": [ai_growth, ai_jobs, ai_chess],
        "comparison": []
    }
)
pg.run()