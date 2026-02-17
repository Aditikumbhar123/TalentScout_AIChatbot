def calculate_score(candidate):
    score = 0

    tech_stack = [t.lower() for t in candidate.get("tech_stack", [])]
    experience = candidate.get("experience", "0")
    position = candidate.get("position", "").lower()

    # =========================
    # Experience Scoring
    # =========================
    try:
        exp = float(experience)
        if exp >= 5:
            score += 30
        elif exp >= 2:
            score += 20
        elif exp >= 1:
            score += 10
    except:
        pass

    # =========================
    # Position-aware scoring
    # =========================
    role_maps = {
        "ai": ["ml", "ai", "tensorflow", "pytorch", "keras", "nlp", "cv", "deep learning"],
        "data": ["sql", "pandas", "numpy", "powerbi", "tableau"],
        "backend": ["python", "java", "node", "flask", "django", "api"],
        "frontend": ["html", "css", "javascript", "react", "vue", "angular"],
        "cloud": ["aws", "azure", "gcp", "docker", "kubernetes", "devops"]
    }

    for role, skills in role_maps.items():
        if role in position:
            for t in tech_stack:
                if any(s in t for s in skills):
                    score += 8   # strong match
                else:
                    score += 1   # weak relevance

    # General skill value
    for t in tech_stack:
        if len(t) > 2:
            score += 2

    # Cap
    if score > 100:
        score = 100

    # =========================
    # Fit Level
    # =========================
    if score >= 75:
        level = "Strong Fit"
    elif score >= 50:
        level = "Moderate Fit"
    else:
        level = "Needs Upskilling"

    return score, level
