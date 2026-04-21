# Project Instructions

This repository represents a personal health optimization system with patient data organized in a structured clinical pipeline.

## Folder Structure

This patient's health data is organized in a numbered clinical pipeline located in **patient_file/**:

- **patient_file/1_data/**: Raw diagnostic data (blood tests, genetic, microbiome, patient profile, etc.)
  - Start with patient_profile.md for demographics and baseline data
  - This folder is readonly for you. DO NOT modify it.
- **patient_file/2_assessments/**: Clinical interpretations and analysis of diagnostic data (what does this mean?)
- **patient_file/3_interventions/**: Treatment protocols (current, past, proposed) (what do we do about it?)
- **patient_file/4_monitoring/**: Daily metrics, tracking, and outcomes (is it working?)

Additionally, general research is stored outside the patient file:

- **research/**: General evidence reviews, literature deep dives, practitioner analyses (what does the science say?)
  - Organized by topic (e.g., `research/sibo/`, `research/thiamine/`)
  - This is reference material — not part of the patient's clinical record

You are responsible to update the patient's file accordingly like a medical professional when editing files.