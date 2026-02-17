import re

# =========================
# SAFE STRING HANDLER
# =========================

def safe_text(text):
    if text is None:
        return ""
    return str(text).strip()

# =========================
# VALIDATORS
# =========================

def validate_non_empty(text):
    text = safe_text(text)
    return bool(text)

def validate_name(name):
    name = safe_text(name)
    if not name:
        return False
    return bool(re.match(r"^[A-Za-z ]{2,50}$", name))

def validate_email(email):
    email = safe_text(email)
    if not email:
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def validate_phone(phone):
    phone = safe_text(phone).replace(" ", "").replace("-", "")
    if not phone:
        return False
    pattern = r"^\+?\d{10,15}$"
    return bool(re.match(pattern, phone))

def validate_experience(exp):
    exp = safe_text(exp)
    if not exp:
        return False
    try:
        val = float(exp)
        return val >= 0 and val <= 50
    except:
        return False

def validate_position(position):
    position = safe_text(position)
    return len(position) >= 2

def validate_tech_stack(tech):
    tech = safe_text(tech)
    if not tech:
        return False
    items = [t.strip() for t in tech.split(",") if t.strip()]
    return len(items) >= 1
