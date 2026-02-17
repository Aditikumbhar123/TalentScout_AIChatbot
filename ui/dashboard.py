import streamlit as st

def show_dashboard(candidate, score, level):
    st.sidebar.markdown("## 📄 Candidate Summary")

    st.sidebar.markdown(f"**Name:** {candidate.get('name')}")
    st.sidebar.markdown(f"**Position:** {candidate.get('position')}")
    st.sidebar.markdown(f"**Experience:** {candidate.get('experience')} yrs")

    st.sidebar.markdown("### 🧠 Skills")
    for skill in candidate.get("tech_stack", []):
        st.sidebar.markdown(f"- {skill}")

    st.sidebar.markdown("### 🎯 Match Score")
    st.sidebar.progress(score/100)

    st.sidebar.markdown(f"**Fit Level:** {level}")
