from ollama_helper import ask_llm

def generate_explanation(patient, medicine, warnings, mode, language):

    prompt = f"""
    You are an advanced healthcare explanation agent.

    Patient:
    Age: {patient['age']}
    Conditions: {patient['conditions']}
    Current Medications: {patient['current_medications']}

    Medicine:
    {medicine}

    Warnings:
    {warnings}

    Response Mode:
    {mode}

    Language:
    {language}

    Instructions:

    If mode = doctor:
    - use concise clinical terminology

    If mode = patient:
    - use extremely simple language

    Return:
    1. Medication Purpose
    2. Key Risks
    3. Important Side Effects
    4. Medication Timing
    5. Final Recommendation

    Keep response concise.
    """

    return ask_llm(prompt)