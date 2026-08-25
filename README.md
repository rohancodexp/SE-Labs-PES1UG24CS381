# Patient Health Record Consent Management System (PHRCMS)
## Software Engineering Lab 1 — Problem Statement #13 (Healthcare & Telemedicine)

This repository contains the deliverables for the **Software Engineering Lab 1** project. 

The project centers on requirements engineering and use-case modeling for a patient-centric health data gateway where patients explicitly manage granular, time-bound consent permissions for clinics, diagnostic labs, and consulting doctors to access their medical history.

---

## 1. System Scope & Boundary

### In-Scope (PHRCMS)
* **Consent Granting**: Allowing patients to grant access to specific diagnostic records to verified clinic doctors with an explicit expiration timestamp.
* **Consent Revocation**: Allowing patients to terminate access early.
* **Access Control**: Validating that active, unexpired consent exists before permitting a doctor to view a record.
* **Audit Trail**: Logging all grant, revoke, and access events permanently in an append-only log.

### Out-of-Scope (External)
* Authentication/Identity management.
* Direct hospital ERP functions (billing, appointments, prescriptions).
* Storing full medical record details (only access metadata is handled).

---

## 2. Actors & Stakeholders

1. **Patient (Primary)**: Grants/revokes consent, views active consents, and maintains full control over diagnostic records.
2. **Clinic Doctor (Healthcare Provider)**: Requests and views diagnostic records when active, valid consent exists.
3. **Clinic Administrator (Administrative Authority)**: Maintains trust in the system by verifying the credentials and registration status of clinic doctors.

---

## 3. Main Use Cases

* **UC-01**: Grant Time-Bounded Consent (Patient)
* **UC-02**: Revoke Active Consent (Patient)
* **UC-03**: View Consent Registry (Patient)
* **UC-04**: Access Diagnostic Records (Clinic Doctor)
* **UC-05**: Manage Doctor Verification (Clinic Administrator)
* **UC-06**: Verify Active Consent (System Use Case, included in `UC-04`)

---

## 4. Repository Structure

```text
SE-Labs-PES1UG24CS381/
│
├── README.md                              # Root project overview
│
└── Lab1/
    │
    ├── README.md                          # Lab 1 specific guide
    │
    ├── 01_Requirements_Table.md           # Markdown version of requirements
    ├── 01_Requirements_Table.xlsx         # Formatted Excel sheet of requirements
    ├── 01_Requirements_Table.pdf          # PDF export of requirements
    │
    ├── 02_UseCase_Diagram.puml            # PlantUML source code
    ├── 02_UseCase_Diagram.png             # Rendered PNG diagram
    ├── 02_UseCase_Diagram.pdf             # PDF version of the diagram
    │
    ├── 03_UseCase_Flow_Specification.md   # Markdown version of flow spec
    ├── 03_UseCase_Flow_Specification.docx # Word document (.docx) flow spec
    └── 03_UseCase_Flow_Specification.pdf  # PDF version of the flow spec
```

---

## 5. Academic Details
* **Student Name / USN**: Rohan (PES1UG24CS381)
* **Subject**: Software Engineering Lab 1 (CS381)
* **Domain**: Healthcare & Telemedicine (Consent Management)
