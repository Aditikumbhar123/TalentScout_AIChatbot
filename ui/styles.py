import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
    .chat-box {
        padding: 12px;
        border-radius: 12px;
        margin: 5px 0;
    }
    .assistant {
        background-color: #1f2937;
        color: white;
    }
    .user {
        background-color: #2563eb;
        color: white;
        text-align: right;
    }
    .card {
        background-color: #0f172a;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        color: white;
    }
    .score-card {
        background: linear-gradient(135deg,#2563eb,#7c3aed);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align:center;
        font-size: 22px;
    }
    </style>
    """, unsafe_allow_html=True)
