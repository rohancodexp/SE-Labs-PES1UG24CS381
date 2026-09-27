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
├── LAB3/                           # Lab 3: Component Modelling & Architectural Pattern Selection
│   ├── PES1UG24CS381_LAB03.pdf     # Combined Lab 3 Comprehensive Submission PDF
│   ├── PES1UG24CS381_LAB03.docx    # Combined Lab 3 Comprehensive Submission Word Doc
│   ├── PHRCMS_Lab3_Justification.pdf # 1-Page Architectural Justification PDF
│   ├── PHRCMS_Lab3_Justification.docx # 1-Page Architectural Justification Word Doc
│   ├── PHRCMS_Component_Diagram.pdf # Single-Page UML Component Diagram PDF
│   ├── Lab_3_Architecture_Student_handout.pdf # Lab 3 Assignment Handout
│   ├── component-diagram.png       # UML 2.5 Component Diagram (PNG)
│   ├── component-diagram.svg       # UML 2.5 Component Diagram (Vector SVG)
│   └── README.md                   # Lab 3 Architectural Specifications & Traceability
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

### [Lab 3: Component Modelling & Architectural Pattern Selection](./LAB3/README.md)
* **Goal**: Evaluate candidate software architectural styles, select the optimal pattern for PHRCMS with quantitative decision matrix and ADRs, construct a UML 2.5 Component Model with provided/required interfaces, and perform STRIDE threat modeling & latency budget analysis.
* **Key Deliverables**:
  * **Selected Architecture**: Layered Modular Service-Oriented Architecture (SOA) with Zero-Trust Policy Enforcement Point (PEP) and asynchronous append-only audit trail.
  * **Subsystems & Components**: 4 architectural tiers, 9 decoupled components, 4 persistent data stores with formal ball-and-socket interfaces.
  * **Key Architectural Decisions (ADRs)**: Zero-Trust PEP/PDP separation, dual-store consistency (PostgreSQL + Redis), cryptographic SHA-256 hash-chained audit logging.
  * **Performance & Security Proof**: Sub-30ms authorization latency budget (< 500ms SLA, NFR-002) and STRIDE threat mitigation matrix.
  * [Combined Submission Document (PDF)](./LAB3/PES1UG24CS381_LAB03.pdf)
  * [Combined Submission Document (DOCX)](./LAB3/PES1UG24CS381_LAB03.docx)
  * [1-Page Architectural Justification (PDF)](./LAB3/PHRCMS_Lab3_Justification.pdf)
  * [1-Page Architectural Justification (DOCX)](./LAB3/PHRCMS_Lab3_Justification.docx)
  * [Single-Page Component Diagram (PDF)](./LAB3/PHRCMS_Component_Diagram.pdf)
  * [UML 2.5 Component Diagram (PNG)](./LAB3/component-diagram.png)
  * [UML 2.5 Component Diagram (SVG)](./LAB3/component-diagram.svg)
  * [Official Lab Handout (PDF)](./LAB3/Lab_3_Architecture_Student_handout.pdf)

---

## End-to-End Traceability (Requirements → User Stories → Components)

| Req ID | Type | Requirement Summary | Epic & User Story | Realizing Component | Provided Interface | Data Store |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-001** | Functional | Grant time-bounded access to verified doctors | `US-01: Grant Time-Bounded Consent` (5 SP) | Consent Management Component | `IConsentGrant` | PostgreSQL & Redis Cache |
| **FR-002** | Functional | Revoke active consent prior to expiration | `US-02: Revoke Active Consent` (3 SP) | Consent Management Component | `IConsentRevoke` | PostgreSQL & Redis Cache (Eviction) |
| **FR-003** | Functional | Display real-time list of active/expired consents | `US-03: View Consent Registry` (3 SP) | Consent Management Component | `IConsentQuery` | PostgreSQL (`consents` view) |
| **FR-004** | Functional | Doctor access to diagnostic records under consent | `US-04: Access Diagnostic Records` (5 SP) | Access Authorization Component (PEP) & Diagnostic Record Component | `IRecordAccessDecision`, `IDiagnosticRecordFetch` | Redis Cache & S3 Encrypted Store |
| **FR-005** | Functional | Clinic Admin manages doctor verification status | `US-06: Manage Doctor Verification` (3 SP) | Doctor Verification Component | `IDoctorAdminService`, `IDoctorVerificationCheck` | PostgreSQL (`doctors` table) |
| **NFR-001** | Non-Functional| Permanent append-only audit trail logging | `US-05: Enforce Audit Logging` (3 SP) | Append-Only Immutable Audit Trail Component | `IAuditPublisher`, `IAuditQuery` | Append-Only Cryptographic Ledger |
| **NFR-002** | Non-Functional| Access authorization latency < 500ms | `US-05: Enforce Audit Logging` (-) | Access Authorization Component (PEP) & API Gateway | `IPolicyEnforcement` | Fast Active Consent Cache (Redis) |
