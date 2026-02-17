# utils.py

import re

def validate_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email)

def validate_phone(phone):
    pattern = r"^[0-9]{10,15}$"
    return re.match(pattern, phone)

def parse_tech_stack(text):
    # Convert "Python, Django, ML" → ["Python", "Django", "ML"]
    return [tech.strip() for tech in text.split(",") if tech.strip()]
