# File Migration Mapping & Architecture Transition Guide
**Course Code:** 02BMSBI24365 — AI and ML in Bioinformatics  
**Audience:** Students & Instructor, M.Sc. Bioinformatics, Garden City University (GCU)  

This guide provides a direct lookup table showing where existing files from the initial `Day1/` and `Day2/` folders have moved within the new semantic repository structure.

---

## 1. Quick Summary of Structure Changes

* **Lecture Material (`units/`):** Organized by syllabus unit and sub-module (e.g., `units/unit_01_foundations/`).
* **Cross-Cutting Guides (`supplementary_resources/`):** Practical setups and tools that span the whole semester (Git/GitHub, Conda).
* **Assessments (`assessments/`):** Self-evaluations, readiness checks, and unit quizzes without exposed answers.
* **Faculty Workspace (`instructor_resources/`):** Teacher lesson plans, session day logs, and solution keys (kept strictly local via `.gitignore`).
* **Central Datasets (`datasets/`):** Central location for all biological data tables, FASTA files, and accessions.

---

## 2. Complete File Migration Mapping Table

| Original File Location | New Semantic Location | Target Audience | Description |
|---|---|---|---|
| `Day1/course_unit_details.md` | [units/README.md](units/README.md) | Students & Faculty | Complete 4-unit syllabus guide with biological analogies |
| `Day1/career_opportunities_and_usecases.md` | [units/unit_01_foundations/career_perspectives.md](units/unit_01_foundations/career_perspectives.md) | Students | Industry domains, role alignment & applied use cases |
| `Day1/student_assessment_quiz.md` | [assessments/diagnostic_baseline_quiz.md](assessments/diagnostic_baseline_quiz.md) | Students | Baseline readiness check (Python, Math, Biology) |
| `Day1/Day1_Master_Kickoff_Agenda.md` | `instructor_resources/lesson_plans/Day_01_Kickoff.md` | Instructor (Local) | Kickoff session agenda, timing, and facilitation notes |
| `Day2/1.1_Introduction_to_Machine_Learning_in_Bioinformatics.ipynb` | [units/unit_01_foundations/1.1_intro_ml_in_bioinformatics.ipynb](units/unit_01_foundations/1.1_intro_ml_in_bioinformatics.ipynb) | Students | Interactive lecture notebook covering ML foundations |
| `Day2/Student_Biological_Problem_Questionnaire.ipynb` | [units/unit_01_foundations/problem_formulation_tool.ipynb](units/unit_01_foundations/problem_formulation_tool.ipynb) | Students | Interactive 5-step problem framing & model selector tool |
| `Day2/Day2_Master_ML_Theory_Primer.md` | [units/unit_01_foundations/ml_theory_primer.md](units/unit_01_foundations/ml_theory_primer.md) | Students | Visual ML vocabulary, representations, and terminology |
| `Day2/Day2_DeepDive_Regression.md` | [units/unit_01_foundations/deep_dive_regression.md](units/unit_01_foundations/deep_dive_regression.md) | Students | Conceptual deep-dive on regression and continuous biological prediction |
| `Day2/Day2_DeepDive_Classification.md` | [units/unit_02_classical_ml/deep_dive_classification.md](units/unit_02_classical_ml/deep_dive_classification.md) | Students | Deep-dive on discrete decision boundaries & diagnosis models |
| `Day2/Day2_DeepDive_Unsupervised.md` | [units/unit_02_classical_ml/deep_dive_unsupervised.md](units/unit_02_classical_ml/deep_dive_unsupervised.md) | Students | Deep-dive on clustering, PCA, and subtype discovery |
| `Day2/Conda_Environment_Crash_Course.md` | [supplementary_resources/conda_environment_guide.md](supplementary_resources/conda_environment_guide.md) | Students | Cross-cutting Conda/Mamba bioinformatics environment setup |
| `Day2/Git_GitHub_Crash_Course.md` | [supplementary_resources/git_workflow_guide.md](supplementary_resources/git_workflow_guide.md) | Students | Cross-cutting Git and GitHub workflow reference |
| `Day2/Day2_Master_Agenda.md` | `instructor_resources/lesson_plans/Day_02_Primer.md` | Instructor (Local) | Day 2 master schedule, timing, and teaching plan |
| `Day2/assets/*.png` | [units/unit_01_foundations/assets/](units/unit_01_foundations/assets/) | Media | Infographics, flowchart diagrams, and visual metaphors |

---

## 3. How to Reference Files in Code and Prompts

* **In Notebooks:** Always access datasets using `../../datasets/raw/<filename>`
* **In Local Markdown:** Visual figures and diagrams reside in that unit's local `assets/` subfolder (e.g., `![Workflow](assets/diagram.png)`)
* **When Chatting with AI:** Cite files by their semantic names (e.g., `"Refer to units/unit_01_foundations/1.1_intro_ml_in_bioinformatics.ipynb"`)
