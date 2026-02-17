from llm import call_llm

def generate_feedback(candidate, score, level):
    prompt = f"""
You are an AI career coach.

Candidate Profile:
Name: {candidate.get("name")}
Position: {candidate.get("position")}
Experience: {candidate.get("experience")}
Tech Stack: {', '.join(candidate.get("tech_stack", []))}

Score: {score}/100
Fit Level: {level}

Generate professional feedback with:
1. Resume relevance to position
2. Skill alignment
3. Readiness level
4. Strengths
5. Weak areas
6. Improvement suggestions
7. Learning path recommendation
"""

    feedback = call_llm(prompt)
    return feedback
