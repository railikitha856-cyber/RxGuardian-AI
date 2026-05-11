import json

def load_patient_data():
    with open("sample_fhir_data.json", "r") as file:
        data = json.load(file)
    return data["patient"]

def analyze_risk(new_medicine):

    patient = load_patient_data()

    warnings = []

    severity = "LOW"

    current_meds = patient["current_medications"]
    allergies = patient["allergies"]
    conditions = patient["conditions"]

    medicine_lower = new_medicine.lower()

    # Interaction checks

    if medicine_lower == "ibuprofen":

        if "Aspirin" in current_meds:
            warnings.append(
                "Risk: Ibuprofen + Aspirin increases bleeding risk"
            )
            severity = "HIGH"

        if "Hypertension" in conditions:
            warnings.append(
                "Risk: may raise blood pressure"
            )

    if medicine_lower == "amoxicillin":

        if "Penicillin" in allergies:
            warnings.append(
                "ALERT: Possible severe allergic reaction"
            )
            severity = "CRITICAL"

    # Risk score

    risk_score = min(len(warnings) * 40, 100)

    # Emergency flag

    emergency = severity == "CRITICAL"

    return {
        "patient": patient,
        "warnings": warnings,
        "risk_score": risk_score,
        "severity": severity,
        "emergency": emergency
    }