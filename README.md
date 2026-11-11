# Software Engineering Laboratory Portfolio

**Student:** Rohan M\
**SRN:** PES1UG24CS381\
**Course:** Software Engineering Laboratory\
**Repository:**
[SE-Labs-PES1UG24CS381](https://github.com/rohancodexp/SE-Labs-PES1UG24CS381)

This repository contains laboratory submissions, implementation work,
testing evidence, diagrams, reports, and other deliverables completed
for the Software Engineering Laboratory course.

## Laboratory Index

  ---------------------------------------------------------------------------------------
  Lab                          Topic / Project   Main contents          Status
  ---------------------------- ----------------- ---------------------- -----------------
  [Lab 1](./LAB1/)             Requirements      Requirements, use-case Folder present
                               Engineering and   flow, UML use-case     
                               UML Use-Case      diagram, submission    
                               Modelling ---     documents              
                               Patient Health                           
                               Record Consent                           
                               Management System                        
                               (PHRCMS)                                 

  [Lab 2](./LAB2/)             Agile Backlog     Epics, product         Folder present
                               Creation and      backlog, sprint        
                               Sprint Simulation planning/simulation,   
                               in Jira           Jira screenshots,      
                                                 reflections and report 

  [Lab 3](./LAB3/)             Component         Component diagram,     Folder present
                               Modelling and     architecture           
                               Architectural     justification,         
                               Pattern Selection specifications and     
                               --- PHRCMS        submission documents   

  [Lab                         Vibe Coding ---   Game implementation,   Folder present
  4](./LAB4/12_maze_runner/)   Pygame Maze       requirements,          
                               Runner            before/after           
                                                 demonstration videos,  
                                                 work report and        
                                                 conversation record    

  [Lab 5](./LAB5/)             Lab 5             See the [Lab 5         Folder present;
                                                 folder](./LAB5/) for   summary to be
                                                 its problem statement, completed
                                                 implementation and     
                                                 evidence               

  [Lab 6](./LAB6/)             Code and Branch   Application, separate  Committed
                               Coverage Analysis code-coverage and      previously
                               --- Electricity   branch-coverage test   
                               Bill Application  suites, README and     
                                                 terminal evidence      

  [Lab 7](./Lab%207/)          Fuzz Testing for  Hypothesis-based       Committed; verify
                               Input Validation  tests,                 required
                               Bugs ---          input-validation fixes filenames against
                               Electricity Bill  and README             faculty
                               Application                              instructions
  ---------------------------------------------------------------------------------------

> **Note:** The Lab 5 summary is intentionally kept general until its
> exact title and deliverables are confirmed. The Lab 6 and Lab 7 status
> descriptions reflect the recorded local Git commits; check the linked
> folders on GitHub for the latest visible contents.

## Repository Structure

``` text
SE-Labs-PES1UG24CS381/
├── LAB1/
├── LAB2/
├── LAB3/
├── LAB4/
│   └── 12_maze_runner/
├── LAB5/
├── LAB6/
├── Lab 7/
└── README.md
```

Folder names and capitalization are retained as used in the repository.

## Lab Highlights

### Labs 1--3: Patient Health Record Consent Management System

The first three labs use the PHRCMS scenario, a healthcare and
telemedicine system focused on time-bound consent permissions for
controlled access to patient health records.

-   **Lab 1:** Requirements Engineering and UML Use-Case Modelling.
-   **Lab 2:** Agile backlog creation and sprint simulation using Jira.
-   **Lab 3:** Component modelling and architectural pattern selection.

### Lab 4: Pygame Maze Runner

A Vibe Coding project implementing a Maze Runner game. The project
folder contains the game code and supporting before/after demonstration
and reporting artefacts.

### Lab 5

See the [Lab 5 directory](./LAB5/) for the submitted work. This
portfolio summary will be expanded when the exact Lab 5 title and
deliverables are confirmed.

### Lab 6: Code and Branch Coverage Analysis

The Electricity Bill application was tested using separate test suites
for code coverage and branch coverage.

Recorded results: - Code coverage: **100%** (32 of 32 statements). -
Branch coverage: **100%** (22 of 22 branches). - Code-coverage suite:
**12 tests passed**. - Branch-coverage suite: **19 tests passed**.

The Lab 6 folder contains the application, test files, README and
coverage evidence.

### Lab 7: Fuzz Testing for Input Validation Bugs

The Electricity Bill application was examined using Hypothesis-based
property/fuzz tests across: - `units_consumed()` - `daily_average()` -
`tariff_rate()`

The tests exposed unexpected exceptions for `None` inputs and a reversed
meter-reading edge case. Input validation was strengthened and the
recorded final test run showed **7 tests passed**.

**Filename note:** The current Lab 7 folder uses `electricity_bill.py`
and `test_electricity_bill.py`. The faculty announcement also refers to
`processor.py` and `test_processor.py`; confirm the required naming
convention with the instructor before treating the Lab 7 submission as
fully compliant.

## Tools and Technologies

Tools documented across the repository include:

-   Python
-   pytest
-   Hypothesis
-   Jira
-   UML modelling artefacts
-   Pygame
-   Git and GitHub

Specific tools and dependencies for each lab are documented in that
lab's own folder where available.

## How to Navigate

1.  Open the relevant lab folder from the [laboratory
    index](#laboratory-index).
2.  Read its `README.md` (if present) for the lab-specific overview and
    instructions.
3.  Refer to the source files, diagrams, screenshots, videos and reports
    included in that folder.
4.  Use the lab-specific handout as the authority for its exact
    submission requirements.

## Repository Maintenance

Each lab is maintained in its own directory to keep source code,
evidence and reports organised. Updates are committed and pushed to the
`main` branch.

------------------------------------------------------------------------

*This README is the repository-level index. For detailed objectives,
execution instructions, test commands and evidence, refer to the README
and documentation inside each lab folder.*
