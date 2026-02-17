import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ ACTIVE MODEL
            messages=[
                {"role": "system", "content": "You are a technical interviewer generating interview questions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600
        )

        # ✅ Safe extraction
        if response and response.choices:
            content = response.choices[0].message.content
            if content:
                return content.strip()

        return ""

    except Exception as e:
        print("LLM ERROR:", e)
        return ""

def generate_feedback(candidate, score, level):
    prompt = f"""
Generate professional HR feedback for candidate.

Details:
Name: {candidate.get('name')}
Position: {candidate.get('position')}
Score: {score}
Level: {level}
Skills: {candidate.get('tech_stack')}

Provide:
1. Strengths
2. Weaknesses
3. Learning Suggestions
4. Hiring Recommendation
"""
    return call_llm(prompt)
