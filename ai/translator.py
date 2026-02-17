from llm import call_llm

LANGUAGE_CODES = {
    "English": "English",
    "Hindi": "Hindi",
    "German": "German",
    "French": "French",
    "Spanish": "Spanish",
    "Marathi": "Marathi",
    "Tamil": "Tamil",
    "Telugu": "Telugu",
    "Kannada": "Kannada",
    "Malayalam": "Malayalam"
}

def translate(text, language):
    if language == "English":
        return text  # no translation needed

    target_lang = LANGUAGE_CODES.get(language, language)

    prompt = f"""
Translate the following text into {target_lang}.
Keep meaning natural and professional.

Text:
{text}
"""

    result = call_llm(prompt)
    if result:
        return result.strip()
    return text
