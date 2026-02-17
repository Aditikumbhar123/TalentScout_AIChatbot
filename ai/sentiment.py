from llm import call_llm

def analyze_sentiment(text):
    text = text.lower()

    nervous_words = ["not sure", "maybe", "i think", "probably", "little", "basic"]
    confident_words = ["built", "developed", "led", "designed", "implemented", "production", "deployed"]

    for w in nervous_words:
        if w in text:
            return "Nervous"

    for w in confident_words:
        if w in text:
            return "Confident"

    # fallback to LLM
    prompt = f"""
Analyze the confidence level of the user input:

"{text}"

Classify strictly as:
- Confident
- Nervous
- Neutral

Return only one word.
"""
    result = call_llm(prompt)
    return result.strip() if result else "Neutral"
