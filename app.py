from ui.styles import apply_styles
from ui.dashboard import show_dashboard
from ai.sentiment import analyze_sentiment
from ai.translator import translate
from ai.feedback import generate_feedback

import streamlit as st
from memory import init_candidate
from conversation import get_next_question, process_input
from scoring import calculate_score
from llm import call_llm

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="TalentScout AI Hiring Assistant", layout="wide")
apply_styles()

# =========================
# SIDEBAR
# =========================
language = st.sidebar.selectbox("🌍 Language", ["English", "Hindi", "German", "French", "Spanish", "Marathi", "Tamil", "Telugu", "Kannada", "Malayalam"])

st.sidebar.markdown("---")
st.sidebar.markdown("## 🤖 TalentScout AI")
st.sidebar.markdown("AI-powered Hiring Assistant")
st.sidebar.markdown("LLM • Prompt Engineering • Smart Scoring")

# =========================
# TITLE
# =========================
st.title("🤖 TalentScout AI Hiring Assistant")
st.caption("AI-powered intelligent candidate screening system")

# =========================
# INIT SESSION STATE
# =========================
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.stage = "NAME"
    st.session_state.candidate = init_candidate()
    st.session_state.messages = []
    st.session_state.questions = ""
    st.session_state.completed = False
    st.session_state.sentiment = "Neutral"
    st.session_state.score = None
    st.session_state.level = None
    st.session_state.feedback = None

    welcome_msg = "Hello! I'm TalentScout Hiring Assistant 🤖\nLet's begin your screening process.\n\nWhat is your full name?"
    welcome_msg = translate(welcome_msg, language)

    st.session_state.messages.append({
        "role": "assistant",
        "content": welcome_msg
    })

# =========================
# CHAT DISPLAY
# =========================
chat_col, info_col = st.columns([2, 1])

with chat_col:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if not st.session_state.completed:
        user_input = st.chat_input("Type your response...")
    else:
        user_input = None

# =========================
# PROCESS INPUT
# =========================
# =========================
# PROCESS INPUT
# =========================
if user_input:

    # Sentiment
    sentiment = analyze_sentiment(user_input)
    st.session_state.sentiment = sentiment
    st.session_state.candidate["sentiment"] = sentiment

    # User msg
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # AI flow
    new_stage, response = process_input(
        st.session_state.stage,
        user_input,
        st.session_state.candidate
    )

    # ❌ Validation error (same stage = invalid input)
    if response and new_stage == st.session_state.stage:
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
        st.rerun()

    # ✅ Stage update
    st.session_state.stage = new_stage

    # =========================
    # END STAGE
    # =========================
    if new_stage == "END":

        # Questions
        st.session_state.questions = response

        if not st.session_state.questions or len(st.session_state.questions.strip()) == 0:
            fallback = ""
            for tech in st.session_state.candidate["tech_stack"]:
                fallback += f"\n**{tech}**\n"
                fallback += "- Explain core concepts\n"
                fallback += "- Real-world use case\n"
                fallback += "- Common challenges\n\n"
            st.session_state.questions = fallback

        # Show questions
        st.session_state.messages.append({
            "role": "assistant",
            "content": "🧠 **Here are your technical questions:**\n\n" + st.session_state.questions
        })

        # Closing message
        st.session_state.messages.append({
            "role": "assistant",
            "content": "✅ Thank you for your time! Our recruitment team will contact you soon. 👋"
        })

        # =========================
        # AI SCORING
        # =========================
        score, level = calculate_score(st.session_state.candidate)
        st.session_state.score = score
        st.session_state.level = level

        # =========================
        # AI FEEDBACK
        # =========================
        feedback_prompt = f"""
Generate professional HR feedback report.

Candidate Details:
Name: {st.session_state.candidate.get('name')}
Position: {st.session_state.candidate.get('position')}
Experience: {st.session_state.candidate.get('experience')}
Skills: {st.session_state.candidate.get('tech_stack')}
Score: {score}
Fit Level: {level}
Sentiment: {st.session_state.sentiment}

Provide:
1. Strengths
2. Weaknesses
3. Skill Gaps
4. Learning Recommendations
5. Hiring Recommendation
"""
        feedback = call_llm(feedback_prompt)
        st.session_state.feedback = feedback

        st.session_state.completed = True

    else:
        # Normal flow
        next_q = get_next_question(new_stage)
        next_q = translate(next_q, language)
        st.session_state.messages.append({
            "role": "assistant",
            "content": next_q
        })

    st.rerun()


# =========================
# RIGHT PANEL (PERSISTENT UI)
# =========================
with info_col:
    st.markdown("## 📊 AI Insights Panel")

    if st.session_state.score is not None:
        st.markdown(f"""
        <div class="score-card">
            🎯 Score: {st.session_state.score}/100<br>
            🧠 Fit Level: {st.session_state.level}<br>
            😊 Sentiment: {st.session_state.sentiment}
        </div>
        """, unsafe_allow_html=True)

    if st.session_state.feedback:
        st.markdown("## 🧾 AI Feedback")
        st.markdown(st.session_state.feedback)

    if st.session_state.candidate.get("tech_stack"):
        st.markdown("## 🛠️ Skills Extracted")
        for s in st.session_state.candidate["tech_stack"]:
            st.markdown(f"- {s}")
