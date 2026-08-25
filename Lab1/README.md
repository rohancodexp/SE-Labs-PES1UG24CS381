# Software Engineering Lab 1 — Patient Health Record Consent Management System

This directory contains all requirements specification, UML diagrams, and use-case flows for **Problem Statement #13: Healthcare & Telemedicine**.

---

## 1. Requirements Summary

We defined exactly 5 Functional Requirements (FRs) and 2 Non-Functional Requirements (NFRs):

* **FR-001**: Grant time-bounded consent for specific diagnostic records to verified clinic doctors, requiring a valid expiration date and time.
* **FR-002**: Revoke active consent before its scheduled expiration.
* **FR-003**: View active and expired consent registry with real-time status details.
* **FR-004**: Access diagnostic records only when valid active consent exists.
* **FR-005**: Clinic Administrator manages and maintains the verification status of clinic doctors in the system.
* **NFR-001**: Append-only audit trail logging all grant, revoke, and access events.
* **NFR-002**: Consent status verification and access decision response time must be under 500 milliseconds under load.

---

## 2. UML Use-Case Diagram Summary

* **Boundary**: Patient Health Record Consent Management System (PHRCMS)
* **Actors**: Patient, Clinic Doctor, Clinic Administrator
* **Key Relationship**: `UC-04` (Access Diagnostic Records) `«include»` `UC-06` (Verify Active Consent). Consent verification is mandatory for every access attempt.

---

## 3. Core Deliverables

Please find the finalized deliverables below:

### 📄 Requirements Table
* [01_Requirements_Table.xlsx (Excel Format)](01_Requirements_Table.xlsx) - Professionally formatted spreadsheet with proper coloring and borders.
* [01_Requirements_Table.md (Markdown Version)](01_Requirements_Table.md) - GitHub markdown preview.
* [01_Requirements_Table.pdf (PDF Document)](01_Requirements_Table.pdf) - Print-ready landscape PDF.

### 📊 UML Use-Case Diagram
* [02_UseCase_Diagram.puml (PlantUML Source)](02_UseCase_Diagram.puml) - Source file using custom style settings.
* [02_UseCase_Diagram.png (Diagram Image)](02_UseCase_Diagram.png) - High-resolution rendered image.
* [02_UseCase_Diagram.pdf (PDF Document)](02_UseCase_Diagram.pdf) - High-quality vector PDF of the diagram.

### 📝 Use-Case Flow Specification
* [03_UseCase_Flow_Specification.md (Markdown Version)](03_UseCase_Flow_Specification.md) - Text specification for `UC-01` (Grant Time-Bounded Consent).
* [03_UseCase_Flow_Specification.docx (Word Document)](03_UseCase_Flow_Specification.docx) - Formatted Word document with proper headings and spacing.
* [03_UseCase_Flow_Specification.pdf (PDF Document)](03_UseCase_Flow_Specification.pdf) - PDF export.
