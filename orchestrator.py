from agents.safety_agent import evaluate_safety
from agents.recommendation_agent import adherence_advice
from agents.explanation_agent import generate_explanation

def orchestrate_agents(patient, medicine, warnings, risk_data, mode, language):

    safety = evaluate_safety(risk_data)

    recommendations = adherence_advice(medicine)

    explanation = generate_explanation(
        patient,
        medicine,
        warnings,
        mode,
        language
    )

    return {
        "safety_decision": safety,
        "recommendations": recommendations,
        "explanation": explanation
    }