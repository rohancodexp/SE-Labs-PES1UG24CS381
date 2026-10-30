\# LAB 5 – Static Code Analysis



\## Objective

To identify and fix code quality, security, and formatting issues in a Python application using Pylint, Bandit, and Flake8.



\## Project

Society Dues Management – Python application using SQLite.



\## Tools Used

\- Python 3.14.6

\- Pylint 4.1.3

\- Bandit 1.9.4

\- Flake8 7.5.0

\- SQLite

\- Git and GitHub



\## Static Analysis and Remediation



\### 1. Pylint

Identified code quality issues such as missing docstrings, naming convention violations, mutable default arguments, and inconsistent return statements.



Final score: \*\*10.00/10\*\*



\### 2. Bandit

Identified security risks including hardcoded credentials, SQL query construction, and unsafe use of `eval()`.



Remediations included parameterized SQL queries and a restricted arithmetic expression evaluator.



Final result: \*\*No issues identified.\*\*



\### 3. Flake8

Identified formatting issues involving line length and indentation.



Final result: \*\*No violations reported.\*\*



\## Application

The corrected application demonstrates adding society dues, collecting payments, calculating late fees, and listing pending payments.



\## Git Commits

1\. Fix code quality issues identified by Pylint

2\. Fix security vulnerabilities identified by Bandit

3\. Fix formatting issues identified by Flake8



\## Execution

Run the application using:



```bash

python society\_dues.py

```



Expected output:



```text

2500

100

\['A-102']

```

