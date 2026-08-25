# Use-Case Flow Specification

## Use Case: Grant Time-Bounded Consent (UC-01)

**Primary Actor:** Patient  
**Purpose:** Allows a patient to select specific diagnostic records and grant time-bounded access to a verified clinic doctor, with access automatically revoking after the designated expiration timestamp.

### Preconditions
* The Patient is authenticated and logged into the Patient Health Record Consent Management System.
* The Clinic Doctor is registered in the system and verified by the Clinic Administrator.
* The Patient has one or more diagnostic records linked to their account.

### Postconditions
* A consent record is stored in the system database containing the Patient ID, Doctor ID, Record IDs, Grant Timestamp, Expiration Timestamp, and Status set to 'Active'.
* A permanent, unmodifiable event entry is written to the append-only audit trail.
* The designated Clinic Doctor is authorized to access the specified diagnostic records until the expiration timestamp is reached.

### Main Success Scenario
1. Patient selects the 'Grant Record Access' option from the dashboard.
2. System displays a form requesting selection of a verified doctor, selection of diagnostic records, and a specific expiration date and time.
3. Patient searches the verified registry and selects a verified Clinic Doctor.
4. Patient selects one or more specific diagnostic records (e.g., 'Blood Lab Report - 2026-08-20') from their medical history.
5. Patient enters a valid future date and time for the consent's expiration.
6. Patient submits the consent grant request.
7. System validates that the selected doctor is verified, the records belong to the patient, and the expiration timestamp is in the future.
8. System creates the active consent record with the selected parameters and calculated expiration timestamp.
9. System permanently writes the consent grant event (timestamp, Patient ID, Doctor ID, Record IDs, Expiration Timestamp, Action = 'GRANT') to the append-only audit trail.
10. System displays a success message confirming that access has been granted to the doctor until the specified expiration date and time.

### Alternate Flows
**3a. Doctor not verified:**
* 3a1. System checks the doctor's status and determines they are unverified.
* 3a2. System displays an error: 'The selected doctor is currently unverified. Access can only be granted to verified clinic doctors.'
* 3a3. System prompts the patient to select a different doctor.
* 3a4. Flow returns to step 3 of the Main Success Scenario.

**5a. Expiration time in the past or invalid:**
* 5a1. System checks the entered expiration timestamp and determines it is in the past or formatted incorrectly.
* 5a2. System displays an error: 'Expiration timestamp must be a valid date and time in the future.'
* 5a3. System prompts the patient to re-enter the expiration date and time.
* 5a4. Flow returns to step 5 of the Main Success Scenario.

