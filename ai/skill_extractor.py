from llm import call_llm

def extract_skills(text):
    prompt = f"""
Extract only technical skills from this text.

Text:
"{text}"

Rules:
- Return only skill names
- No sentences
- No explanations
- Comma-separated
- Example output: Python, Machine Learning, LLM, RAG, TensorFlow

Output:
"""

    result = call_llm(prompt)

    if not result:
        return []

    skills = [s.strip() for s in result.split(",") if len(s.strip()) > 1]
    return skills
