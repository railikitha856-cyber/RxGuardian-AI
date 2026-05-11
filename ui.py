import streamlit as st
import requests

st.set_page_config(
    page_title="RxGuardian AI",
    layout="wide"
)

st.title("💊 RxGuardian AI")
st.subheader("Multi-Agent Medication Safety Copilot")

# Sidebar

st.sidebar.header("Patient Profile")

st.sidebar.write("Age: 58")
st.sidebar.write("Conditions:")
st.sidebar.write("- Diabetes")
st.sidebar.write("- Hypertension")

st.sidebar.write("Current Medications:")
st.sidebar.write("- Metformin")
st.sidebar.write("- Aspirin")

# Main input

medicine = st.text_input("Enter Medication Name")

mode = st.selectbox(
    "Select Mode",
    ["patient", "doctor"]
)

language = st.selectbox(
    "Language",
    ["english"]
)

if st.button("Analyze Medication"):

    payload = {
        "medicine": medicine,
        "mode": mode,
        "language": language
    }

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json=payload
    )

    data = response.json()

    st.divider()

    # Severity

    severity = data["severity"]

    if severity == "CRITICAL":
        st.error(f"Severity: {severity}")

    elif severity == "HIGH":
        st.warning(f"Severity: {severity}")

    else:
        st.success(f"Severity: {severity}")

    # Risk score

    st.metric(
        label="Risk Score",
        value=f"{data['risk_score']}%"
    )

    # Warnings

    st.subheader("⚠ Safety Warnings")

    for warning in data["warnings"]:
        st.write(f"- {warning}")

    # Recommendations

    st.subheader("✅ Adherence Tips")

    for tip in data["adherence_tips"]:
        st.write(f"- {tip}")

    # Agent Trace

    st.subheader("🤖 Agent Collaboration Trace")

    for trace in data["agent_trace"]:
        st.write(f"- {trace}")

    # AI Analysis

    st.subheader("🧠 Clinical Analysis")

    st.write(data["analysis"])