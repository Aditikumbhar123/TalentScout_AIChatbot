from ai.skill_extractor import extract_skills

def get_next_question(stage):
    if stage == "NAME":
        return "What is your full name?"
    if stage == "EMAIL":
        return "What is your email address?"
    if stage == "PHONE":
        return "What is your phone number?"
    if stage == "POSITION":
        return "Which position are you applying for?"
    if stage == "EXPERIENCE":
        return "How many years of experience do you have?"
    if stage == "TECH_STACK":
        return "Describe your technical skills (you can write in sentences too):"
    if stage == "END":
        return "Processing your profile..."
    return ""


def process_input(stage, user_input, candidate):
    text = user_input.strip()

    # NAME
    if stage == "NAME":
        if len(text) < 2 or not text.replace(" ", "").isalpha():
            return "NAME", "❌ Invalid name. Enter proper full name."
        candidate["name"] = text
        return "EMAIL", None

    # EMAIL
    if stage == "EMAIL":
        if "@" not in text or "." not in text:
            return "EMAIL", "❌ Invalid email format. Example: name@gmail.com"
        candidate["email"] = text
        return "PHONE", None

    # PHONE
    if stage == "PHONE":
        if not text.isdigit() or len(text) < 10 or len(text) > 15:
            return "PHONE", "❌ Invalid phone number. Enter 10–15 digits."
        candidate["phone"] = text
        return "POSITION", None

    # POSITION
    if stage == "POSITION":
        if len(text) < 2:
            return "POSITION", "❌ Invalid position name."
        candidate["position"] = text
        return "EXPERIENCE", None

    # EXPERIENCE
    if stage == "EXPERIENCE":
        if not text.isdigit():
            return "EXPERIENCE", "❌ Enter experience in numbers only."
        candidate["experience"] = int(text)
        return "TECH_STACK", None

    # TECH STACK (🔥 AI extraction)
    # TECH STACK (🔥 AI extraction + question generation)
    if stage == "TECH_STACK":
        skills = extract_skills(text)

    if not skills:
        return "TECH_STACK", "❌ I couldn't detect technical skills. Please mention skills like Python, ML, React, SQL, etc."

    candidate["tech_stack"] = skills

    # ===== QUESTION GENERATION PROMPT =====
    prompt = f"""
You are a technical interviewer.

Candidate skills: {', '.join(skills)}

Generate 3 interview questions for EACH skill.
Each skill must have:
1. Conceptual question
2. Practical question
3. Scenario-based question

Format strictly like:

Python:
1. Question
2. Question
3. Question

Machine Learning:
1. Question
2. Question
3. Question

LLM:
1. Question
2. Question
3. Question

RAG:
1. Question
2. Question
3. Question
"""

    from llm import call_llm
    questions = call_llm(prompt)

    return "END", questions

