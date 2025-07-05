def diagnose_condition(pain_area, answers):
    area = pain_area.lower()

    if area == "knee":
        if "injure" in answers[0].lower() and "yes" in answers[1].lower():
            return "You may have a ligament sprain. Please rest, ice the area, and see an orthopedist."
        elif "stiff" in answers[-1].lower():
            return "It could be early arthritis. Consider an X-ray."
        else:
            return "General knee discomfort. Monitor symptoms."

    elif area == "chest":
        if "sharp" in answers[0].lower() and "spread" in answers[1].lower():
            return "Warning: Possible cardiac issue. Consult a doctor immediately."
        elif "acidity" in answers[-1].lower():
            return "Likely acid reflux. Avoid spicy food and try antacids."
        else:
            return "Monitor the pain. If it worsens, seek help."

    elif area == "back":
        if "bend" in answers[2].lower():
            return "It could be a muscle strain. Rest and avoid heavy lifting."
        elif "leg" in answers[3].lower():
            return "Possibly sciatica. Consider physiotherapy."
        else:
            return "General back pain. Try hot compress and rest."

    elif area == "head":
        if "throbbing" in answers[0].lower() and "light" in answers[3].lower():
            return "It may be a migraine. Avoid triggers and consult a neurologist."
        else:
            return "Generic headache. Try hydration and rest."

    elif area == "neck":
        if "stiff" in answers[0].lower():
            return "You may have neck strain. Try gentle stretches and maintain good posture."
        else:
            return "Mild neck discomfort. Monitor and avoid jerky movements."

    elif area == "shoulder":
        if "raise" in answers[1].lower():
            return "Possible rotator cuff strain. Rest and avoid overhead lifting."
        else:
            return "General shoulder pain. Try cold compress and gentle exercise."

    elif area == "elbow":
        if "grip" in answers[2].lower():
            return "May be tennis elbow. Avoid repetitive motion and apply ice."
        else:
            return "Elbow strain. Rest and consider using a brace."

    elif area == "hand":
        if "swollen" in answers[0].lower() or "injure" in answers[3].lower():
            return "Could be a hand sprain or fracture. Consider getting an X-ray."
        else:
            return "Mild hand discomfort. Rest your hand and avoid overuse."

    elif area == "leg":
        if "cramp" in answers[1].lower() or "tight" in answers[1].lower():
            return "Likely a muscle cramp. Try hydration and gentle massage."
        elif "injure" in answers[2].lower():
            return "Leg injury suspected. Use RICE method and consult a doctor."
        else:
            return "General leg ache. Rest and elevate your leg."

    # Fallback diagnosis
    return "Sorry, unable to diagnose precisely. Please consult a healthcare professional."
