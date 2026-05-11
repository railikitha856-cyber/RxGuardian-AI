def evaluate_safety(risk_data):

    severity = risk_data["severity"]
    warnings = risk_data["warnings"]

    if severity == "CRITICAL":
        return "Immediate medical consultation recommended."

    if severity == "HIGH":
        return "Use with caution and consult healthcare provider."

    if len(warnings) == 0:
        return "No major risks detected."

    return "Monitor symptoms carefully."