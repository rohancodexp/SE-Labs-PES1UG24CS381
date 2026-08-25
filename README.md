# Software Engineering Lab 1: Requirements Engineering & UML Use-Case Modelling

- **SRN**: PES1UG24CS381
- **Scenario No**: 13
- **Project Title**: Patient Health Record Consent Management System (PHRCMS)
- **Primary Domain**: Healthcare & Telemedicine
- **Target Actors**: Patient, Clinic Doctor, Clinic Administrator

---

## Repository Contents

* `PES1UG24CS381_LAB01.pdf` - Complete Lab 1 submission document containing Requirements Table, UML Use-Case Model details, embedded diagram, and Use-Case Flow Specification.
* `requirements.md` - Complete Requirements Table with exactly 5 functional requirements and 2 non-functional requirements.
* `use-case-flow.md` - One-page Use-Case Flow Specification for the core use case Grant Time-Bounded Consent.
* `use-case-diagram.png` - Rendered UML Use-Case Diagram for the Patient Health Record Consent Management System.
* `README.md` - Repository overview.

---

## Requirements Traceability Matrix

| Requirement | Use Case | Target Actor | Included Verification / Auditing |
| :--- | :--- | :--- | :--- |
| **FR-001** (Grant Consent) | `UC-01: Grant Time-Bounded Consent` | Patient | Patient enters verified doctor and future expiration |
| **FR-002** (Revoke Consent) | `UC-02: Revoke Active Consent` | Patient | Triggers immediate revocation status update |
| **FR-003** (Consent List) | `UC-03: View Consent Registry` | Patient | Real-time status list (active/expired/revoked) |
| **FR-004** (Access Record) | `UC-04: Access Diagnostic Records` | Clinic Doctor | Enforces `UC-06: Verify Active Consent` check |
| **FR-005** (Doctor Verification) | `UC-05: Manage Doctor Verification` | Clinic Administrator | Verification flag managed by clinic administrator |
| **NFR-001** (Audit Trail) | Logging and Auditing | System | Appends to append-only log on grant, revoke, or access |
| **NFR-002** (Response Latency) | `UC-06: Verify Active Consent` | System | Consent validation latency is constrained to < 500ms |
