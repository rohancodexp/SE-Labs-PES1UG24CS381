# Software Engineering Laboratory: PHRCMS

- **Student Reference Number (SRN)**: PES1UG24CS381
- **Student Name**: Rohan M
- **Lab Scenario**: Scenario 13
- **Project Title**: Patient Health Record Consent Management System (PHRCMS)
- **Primary Domain**: Healthcare & Telemedicine
- **Target Actors**: Patient, Clinic Doctor, Clinic Administrator

---

## Repository Overview

This repository contains the complete laboratory submissions, software engineering artifacts, and deliverables for the **Patient Health Record Consent Management System (PHRCMS)**.

```
SE13/
├── LAB1/                           # Lab 1: Requirements Engineering & UML Use-Case Modelling
│   ├── PES1UG24CS381_LAB01.pdf     # Combined Lab 1 Submission PDF
│   ├── PES1UG24CS381_LAB01.docx    # Combined Lab 1 Submission Word Doc
│   ├── requirements.md             # Functional & Non-Functional Requirements Table
│   ├── use-case-flow.md            # Use-Case Flow Specification (Grant Consent)
│   ├── use-case-diagram.png        # UML Use-Case Diagram
│   └── README.md                   # Lab 1 Overview & Traceability Matrix
│
├── LAB2/                           # Lab 2: Agile Backlog Creation & Sprint Simulation in Jira
│   ├── PES1UG24CS381_LAB02.pdf     # Combined Lab 2 Submission PDF
│   ├── PES1UG24CS381_LAB02.docx    # Combined Lab 2 Submission Word Doc
│   ├── Software Engineering - LAB 2.pdf
│   ├── Software Engineering - LAB 2.docx
│   ├── README.md                   # Lab 2 Backlog, Sprints, Reflections & Gallery
│   └── *.png                       # Jira screenshots (Epics, Backlog, Sprints, Burndown)
│
├── .gitignore                      # Git ignore rules for office/temporary files
└── README.md                       # Root Landing Page (This file)
```

---

## Laboratory Index & Deliverables Summary

### [Lab 1: Requirements Engineering & UML Use-Case Modelling](./LAB1/README.md)
* **Goal**: Elicit and document 5 Functional Requirements (FRs) and 2 Non-Functional Requirements (NFRs), construct a UML Use-Case Model with associations/stereotypes, and define a formal Use-Case Flow Specification.
* **Key Deliverables**:
  * [Requirements Specification Table](./LAB1/requirements.md)
  * [UML Use-Case Diagram](./LAB1/use-case-diagram.png)
  * [Use-Case Flow Specification](./LAB1/use-case-flow.md)
  * [Combined Submission Document (PDF)](./LAB1/PES1UG24CS381_LAB01.pdf)
  * [Combined Submission Document (DOCX)](./LAB1/PES1UG24CS381_LAB01.docx)

---

### [Lab 2: Agile Backlog Creation & Sprint Simulation in Jira](./LAB2/README.md)
* **Goal**: Convert Lab 1 requirements into Agile Epics and User Stories, apply Planning Poker and Fibonacci estimation for story points, simulate 2 Sprints with active board transitions (`To Do` $\rightarrow$ `In Progress` $\rightarrow$ `Done`), generate Jira Burndown Charts, and analyze performance.
* **Key Deliverables**:
  * **3 Epics**: Consent Management, Secure Health Record Access, Doctor Verification.
  * **6 User Stories**: Formatted in `As a... I want to... So that...` syntax with acceptance criteria and Fibonacci story points.
  * **Sprint 1 (16 SP)**: Core consent and diagnostic record access workflow completed.
  * **Sprint 2 (6 SP)**: Registry audit visibility and administrative doctor verification completed.
  * **Burndown Chart Analysis**: Evaluated remaining effort vs. ideal guideline.
  * **Reflection Answers**: Detailed analysis of estimation accuracy, backlog prioritization, sprint alignment, and velocity.
  * [Combined Submission Document (PDF)](./LAB2/PES1UG24CS381_LAB02.pdf)
  * [Combined Submission Document (DOCX)](./LAB2/PES1UG24CS381_LAB02.docx)

---

## Requirements to Agile User Story Mapping

| Req ID | Type | Requirement Summary | Epic | User Story | SP | Sprint |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **FR-001** | Functional | Grant time-bounded access to verified doctors | Consent Management | `US-01: Grant Time-Bounded Consent` | 5 | Sprint 1 |
| **FR-002** | Functional | Revoke active consent prior to expiration | Consent Management | `US-02: Revoke Active Consent` | 3 | Sprint 1 |
| **FR-003** | Functional | Display real-time list of active/expired consents | Consent Management | `US-03: View Consent Registry` | 3 | Sprint 2 |
| **FR-004** | Functional | Doctor access to diagnostic records under consent | Secure Health Record Access | `US-04: Access Diagnostic Records` | 5 | Sprint 1 |
| **FR-005** | Functional | Clinic Admin manages doctor verification status | Doctor Verification | `US-06: Manage Doctor Verification` | 3 | Sprint 2 |
| **NFR-001** | Non-Functional| Permanent append-only audit trail logging | Secure Health Record Access | `US-05: Enforce Audit Logging` | 3 | Sprint 1 |
| **NFR-002** | Non-Functional| Access authorization latency < 500ms | Secure Health Record Access | `US-05: Enforce Audit Logging` | - | Sprint 1 |
