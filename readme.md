# RxGuardian AI

FHIR-aware Multi-Agent Medication Safety Copilot

## Problem

Patients frequently misunderstand medications, dangerous drug interactions are overlooked, and healthcare AI systems often provide generic responses without patient-specific context.

## Solution

RxGuardian AI is an interoperable healthcare safety agent that analyzes medication risks, generates personalized explanations, and provides adherence guidance using collaborative healthcare agents.

## Features

- Medication risk analysis
- Drug interaction detection
- Severity scoring
- Patient vs Doctor mode
- Adherence recommendations
- Explainable agent trace
- FHIR-inspired patient context
- Multi-agent orchestration

## Architecture

User → API Gateway → Agent Orchestrator

Agents:
- Safety Agent
- Explanation Agent
- Recommendation Agent

## Tech Stack

- FastAPI
- Streamlit
- Groq API
- Python
- FHIR-inspired healthcare context

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
streamlit run ui.py
```

## Future Scope

- Live FHIR integration
- Multilingual healthcare support
- EHR connectivity
- Clinical co-pilot workflows