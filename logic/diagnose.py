def diagnose_condition(pain_area, answers):
    if pain_area == "knee":
        if "injure" in answers[0].lower() and "yes" in answers[1].lower():
            return "You may have a ligament sprain. Please rest, ice the area, and see an orthopedist."
        elif "stiff" in answers[-1].lower():
            return "It could be early arthritis. Consider an X-ray."
        else:
            return "General knee discomfort. Monitor symptoms."

    elif pain_area == "chest":
        if "sharp" in answers[0].lower() and "spread" in answers[1].lower():
            return "Warning: Possible cardiac issue. Consult a doctor immediately."
        elif "acidity" in answers[-1].lower():
            return "Likely acid reflux. Avoid spicy food and try antacids."
        else:
            return "Monitor the pain. If it worsens, seek help."

    elif pain_area == "back":
        if "bend" in answers[2].lower():
            return "It could be a muscle strain. Rest and avoid heavy lifting."
        elif "leg" in answers[3].lower():
            return "Possibly sciatica. Consider physiotherapy."
        else:
            return "General back pain. Try hot compress and rest."

    elif pain_area == "head":
        if "throbbing" in answers[0].lower() and "light" in answers[3].lower():
            return "It may be a migraine. Avoid triggers and consult a neurologist."
        else:
            return "Generic headache. Try hydration and rest."

    # Default fallback
    return "Sorry, unable to diagnose precisely. Please consult a healthcare professional."
