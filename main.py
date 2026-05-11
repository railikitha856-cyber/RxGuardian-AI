from fastapi import FastAPI
from pydantic import BaseModel
from ollama_helper import ask_llm
from medication_logic import analyze_risk
from agents.safety_agent import evaluate_safety
from agents.recommendation_agent import adherence_advice
from agents.explanation_agent import generate_explanation

app = FastAPI()

class MedicationRequest(BaseModel):
    medicine: str
    mode: str = "patient"
    language: str = "english"

@app.get("/")
def home():
    return {"message": "Medication Safety Copilot Running"}

@app.post("/analyze")
def analyze_medication(req: MedicationRequest):

    risk_data = analyze_risk(req.medicine)

    patient = risk_data["patient"]
    warnings = risk_data["warnings"]
    risk_score = risk_data["risk_score"]
    severity = risk_data["severity"]
    emergency = risk_data["emergency"]

    prompt = f"""
    You are an advanced clinical medication safety assistant.

    Patient Information:
    Age: {patient['age']}
    Conditions: {patient['conditions']}
    Current Medications: {patient['current_medications']}
    Allergies: {patient['allergies']}

    Medication:
    {req.medicine}

    Detected Warnings:
    {warnings}

    Provide response in EXACT format:

    1. Medication Purpose
    2. Key Risks
    3. Side Effects
    4. Safety Recommendation
    5. Best Time To Take
    6. Simple Patient Summary

    Keep response concise, clinical, and patient-friendly.
    """

    safety_decision = evaluate_safety(risk_data)

    advice = adherence_advice(req.medicine)

    response = generate_explanation(
        patient,
        req.medicine,
        warnings,
        req.mode,
        req.language
    )

    agent_trace = [
    "Safety Agent analyzed medication interactions",
    "Recommendation Agent generated adherence guidance",
    "Explanation Agent created patient-specific summary"
   ]

    return {
    "medicine": req.medicine,
    "severity": severity,
    "emergency": emergency,
    "risk_score": risk_score,
    "warnings": warnings,
    "safety_decision": safety_decision,
    "adherence_tips": advice,
    "analysis": response,
    "agent_trace": agent_trace
    }
@app.get("/patient-context")
def patient_context():

    from medication_logic import load_patient_data

    patient = load_patient_data()

    return {
        "resourceType": "PatientContext",
        "patient": patient
    }
@app.get("/health")
def health():

    return {
        "status": "active",
        "agents_online": [
            "Safety Agent",
            "Explanation Agent",
            "Recommendation Agent"
        ]
    }