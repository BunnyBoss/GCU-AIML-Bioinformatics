# Repository Architecture & Folder Structure Plan
**Course Code:** 02BMSBI24365 — AI and Machine Learning in Bioinformatics  
**Audience:** M.Sc. Bioinformatics (Semester III / Year 2), Gordon City University (GCU)  
**Duration:** 12 Weeks (3 Months) + 10 Hands-on Computer Labs  
**Core Deliverables:** Interactive Jupyter Notebooks (`.ipynb`) & Visual Markdown (`.md`) Guides  
**Status:** Finalized Plan for Review

---

## 1. Executive Summary & Core Architectural Strategy

This repository uses a **Hybrid Architecture** combining a semantic unit-centric core with a chronological day-to-day schedule:

* **Semantic Core (`units/` and `labs/`):** Course code, theory, and practical assignments are structured strictly by **Unit and Sub-module**, matching the GCU syllabus audit requirements and making long-term revision straightforward for M.Sc. learners.
* **Chronological Schedule Matrix ([SCHEDULE.md](SCHEDULE.md)):** A centralized schedule maps every lecture day and date (Days 1–24 across 12 weeks) to its corresponding unit notebooks, supplementary guides, assessments, and lab experiments. This keeps pacing clear without cluttering the codebase with brittle `DayXX/` folders.
* **Strict Student vs. Faculty Boundary:** Student materials remain clean and public, while teacher-facing lesson plans, answer keys, and day logs live in `instructor_resources/` inside this local repository, strictly excluded from version control via `.gitignore`.
* **AI/RAG Readability:** Semantic numbering, standard frontmatter skeletons, and clean separation between data, static visuals, and code ensure coding agents (Claude Code, Cursor, Copilot, NotebookLM) index and interact with the repository effectively.

---

## 2. Directory Tree Layout

```text
GCU_ML_AI_Bioinformatics/
│
├── README.md                           # Master syllabus, prerequisites, course overview, quickstart
├── SCHEDULE.md                         # 12-week day-by-day lecture & lab schedule matrix
├── ENVIRONMENT.md                      # Conda / Mamba environment setup instructions
├── requirements.txt                    # Pinned Python package dependencies
├── curriculum.txt                      # Official GCU course specification
├── LICENSE                             # Course material license and academic usage notice
├── .gitignore                          # Ignores instructor_resources/, checkpoints, data caches
├── .pre-commit-config.yaml             # Enforces nbstripout to strip notebook outputs on commit
├── REPOSITORY_STRUCTURE_PLAN.md        # This architectural blueprint
│
├── supplementary_resources/            # Cross-cutting student guides outside official curriculum
│   ├── conda_environment_guide.md      # Detailed Conda/Mamba package & environment walkthrough
│   ├── git_workflow_guide.md           # Git & GitHub crash course for bioinformatics workflows
│   └── python_bio_refresher.md         # Fast NumPy, Pandas, BioPython refresher
│
├── datasets/                           # Centralized data store (single source of truth for all datasets)
│   ├── README.md                       # Data dictionary, biology provenance (GEO, TCGA, PDB), citations
│   ├── raw/                            # Sample datasets (<25MB: CSV, TSV, FASTA, GFF)
│   │   ├── brca_gene_expression.csv
│   │   ├── promoter_sequences.fasta
│   │   └── epigenetic_methylation_sample.csv
│   └── download_scripts/               # Automated fetch scripts for larger public databases
│       └── fetch_geo_data.py
│
├── units/                              # Lecture modules (Student-facing: Theory + Interactive Code)
│   ├── unit_01_foundations/
│   │   ├── 1.1_intro_ml_in_bioinformatics.ipynb
│   │   ├── 1.2_data_preprocessing_and_encoding.ipynb
│   │   ├── 1.3_regression_theory_and_math.md
│   │   ├── 1.4_regression_gene_expression_case_study.ipynb
│   │   ├── career_perspectives.md      # Unit-specific reference guide
│   │   ├── ml_theory_primer.md         # Unit-specific conceptual guide
│   │   ├── deep_dive_regression.md     # Unit-specific math/theory reference
│   │   └── assets/                     # Small unit-specific images, diagrams, infographics
│   │
│   ├── unit_02_classical_ml/
│   │   ├── 2.1_classification_trees_and_forests.ipynb
│   │   ├── 2.2_unsupervised_clustering_and_pca.ipynb
│   │   ├── 2.3_model_evaluation_and_roc_auc.ipynb
│   │   ├── 2.4_scikit_learn_biological_pipelines.ipynb
│   │   ├── deep_dive_classification.md
│   │   ├── deep_dive_unsupervised.md
│   │   └── assets/
│   │
│   ├── unit_03_deep_learning/
│   │   ├── 3.1_ann_foundations_backpropagation.ipynb
│   │   ├── 3.2_keras_tensorflow_bio_workflows.ipynb
│   │   ├── 3.3_cnn_bioimages_and_rnn_sequences.ipynb
│   │   ├── 3.4_transformers_and_protein_llms.ipynb
│   │   └── assets/
│   │
│   └── unit_04_ai_applications/
│       ├── 4.1_multi_omics_disease_prediction.ipynb
│       ├── 4.2_motif_detection_and_protein_families.ipynb
│       ├── 4.3_explainable_ai_shap_and_lime.ipynb
│       └── assets/
│
├── labs/                               # 10 University Lab Experiments (Student-facing practicals)
│   ├── lab_01_expression_preprocessing/
│   │   ├── README.md                   # Objective, background, input data, rubric
│   │   └── Lab_01_Student.ipynb        # Scaffolded exercise notebook with TODOs & assertions
│   ├── lab_02_biological_regression/
│   ├── lab_03_tumor_classification/
│   ├── lab_04_evaluation_metrics_roc/
│   ├── lab_05_unsupervised_pca_clustering/
│   ├── lab_06_ann_keras_workflow/
│   ├── lab_07_histopathology_cnn/
│   ├── lab_08_sequence_classification_1dcnn_lstm/
│   ├── lab_09_xai_shap_biomarkers/
│   └── lab_10_capstone_project/
│
├── assessments/                        # Student-facing knowledge checks & diagnostic tools
│   ├── README.md                       # Self-evaluation instructions
│   ├── diagnostic_baseline_quiz.md     # Initial readiness check (Python, Git, Math, Biology)
│   ├── unit_01_self_check.md
│   ├── unit_02_self_check.md
│   ├── unit_03_self_check.md
│   └── unit_04_self_check.md
│
└── instructor_resources/               # TEACHER-FACING ONLY (Locally managed; listed in .gitignore)
    ├── README.md                       # Facilitation guide & pointer to day log template
    ├── templates/                      # Standard templates for ongoing course operations
    │   └── session_log_template.md     # Standard Day-History Log template (Plan & Actual)
    ├── day_logs/                       # Session-by-session history records (one per lecture day)
    │   ├── Day_01_log.md
    │   ├── Day_02_log.md
    │   └── ...
    ├── lesson_plans/                   # Pedagogical master outlines and discussion prompts
    │   ├── Day_01_Kickoff.md
    │   ├── Day_02_Primer.md
    │   └── ...
    ├── lab_solutions/                  # Master answer keys and executed solution notebooks
    │   ├── Lab_01_Solution.ipynb
    │   └── ...
    └── quiz_keys/                      # Graded quiz rubrics and detailed solutions
        └── diagnostic_baseline_key.md
```

---

## 3. Student-Facing vs. Teacher-Facing Resource Separation

1. **Student Workspace (`units/`, `labs/`, `datasets/`, `assessments/`, `supplementary_resources/`):**
   * Contains interactive theory, runnable code walkthroughs, cross-cutting guides, and scaffolded lab notebooks.
   * Exercises provide clear prompts (`### START CODE HERE ###` ... `### END CODE HERE ###`) and local unit tests (`assert` statements) to give immediate feedback.
   * Quiz files contain self-reflection questions, omitting answer keys.
2. **Teacher Workspace (`instructor_resources/`):**
   * **Local-Only Boundary via `.gitignore`:** `instructor_resources/` lives directly inside this repository on the teacher's local machine for frictionless access, but is strictly added to `.gitignore`.
   * **Never Pushed to Remote:** Because it is ignored by Git, solution notebooks, quiz answer keys, lesson plans, and session logs remain strictly private and will never be committed or pushed to student-facing remotes.
   * **Session-by-Session History Logging (`instructor_resources/day_logs/`):**
     * Maintains a structured record for each teaching day (e.g., `Day_01_log.md`, `Day_02_log.md`).
     * Created using a standardized template (`templates/session_log_template.md`) referenced in `instructor_resources/README.md`.
     * Completed in two distinct phases:
       * **Before Session (Plan):** Target topics, learning objectives, materials/notebooks to run, time allocations.
       * **After Session (Actual):** Actual coverage achieved, deviations from plan, key pedagogical decisions, student questions/pain points encountered, and assigned homework/takeaways.

---

## 4. Asset vs. Dataset Architecture (Explicit Policy)

To eliminate ambiguity across the 12-week course, maintain a strict divide between `assets/` and `datasets/`:

* **Unit Local Assets (`units/unit_XX/assets/`):**
  * Reserved exclusively for **static visual media and lightweight reference figures**.
  * Includes PNG/SVG flowcharts, biological infographics, pathway diagrams, architecture schematics, and micro-tables formatted for visual explanation.
  * Never place raw data files, tabular experimental records, FASTA sequences, or CSV files here.
* **Centralized Datasets (`datasets/raw/` and `datasets/download_scripts/`):**
  * The single source of truth for **all actual datasets** consumed by notebooks and labs across any unit.
  * Contains gene expression matrices (CSV/TSV), DNA/Protein sequence files (FASTA), methylation beta-value tables, and clinical annotation files.
  * Notebooks reference data using standardized paths (e.g., `../../datasets/raw/brca_gene_expression.csv`).
  * A master [datasets/README.md](datasets/README.md) details biological provenance, accession IDs (GEO, TCGA, PDB), dimensions ($N \times P$), and preprocessing status (counts vs. TPM vs. log2).

---

## 5. Optimizing for AI / RAG Interactions & Code Hygiene

### A. Blank Frontmatter Metadata Skeleton
To make every notebook and Markdown document instantly indexable by AI agents (Claude Code, Cursor, Copilot, NotebookLM) and vector search, begin every deliverable with this standardized header:

```markdown
---
unit: "Unit 1: Foundations of Machine Learning for Bioinformatics"
submodule: "1.2 Data Preprocessing & Sequence Encoding"
concepts: ["missing value imputation", "standard scaling", "k-mers", "one-hot encoding"]
dataset: "datasets/raw/promoter_sequences.fasta"
ai_tier: "Tier 1: Conceptual Walkthrough & Code Scaffolding"
---
```

### B. Notebook Output Stripping (`nbstripout`)
* Large image outputs, execution counts, and tracebacks inflate git diffs and break repository searches.
* Configure a pre-commit hook via `.pre-commit-config.yaml` using `nbstripout` so all notebook outputs are automatically stripped before committing, ensuring clean diffs and lean student clones:
  ```yaml
  repos:
    - repo: https://github.com/kynan/nbstripout
      rev: 0.7.1
      hooks:
        - id: nbstripout
  ```

### C. Root License & Academic Usage Notice
* Include a root `LICENSE` file (e.g., MIT for code, CC-BY-4.0 for educational content).
* State clear academic integrity expectations and guidelines regarding student usage and AI-assisted coursework.

---

## 6. Migration Map for Existing Day 1 and Day 2 Files

| Current Location | Proposed Target Location | Category |
|---|---|---|
| `Day1/Day1_Master_Kickoff_Agenda.md` | `instructor_resources/lesson_plans/Day_01_Kickoff.md` | Instructor (Local) |
| `Day1/course_unit_details.md` | `units/README.md` | Student Core |
| `Day1/career_opportunities_and_usecases.md` | `units/unit_01_foundations/career_perspectives.md` | Student Unit 1 |
| `Day1/student_assessment_quiz.md` | `assessments/diagnostic_baseline_quiz.md` | Student Assessment |
| `Day2/1.1_Introduction_to_Machine_Learning_in_Bioinformatics.ipynb` | `units/unit_01_foundations/1.1_intro_ml_in_bioinformatics.ipynb` | Student Unit 1 |
| `Day2/Student_Biological_Problem_Questionnaire.ipynb` | `units/unit_01_foundations/problem_formulation_tool.ipynb` | Student Unit 1 |
| `Day2/Conda_Environment_Crash_Course.md` | `supplementary_resources/conda_environment_guide.md` *(summarized in `ENVIRONMENT.md`)* | Student Supplementary |
| `Day2/Git_GitHub_Crash_Course.md` | `supplementary_resources/git_workflow_guide.md` | Student Supplementary |
| `Day2/Day2_DeepDive_Classification.md` | `units/unit_02_classical_ml/deep_dive_classification.md` | Student Unit 2 |
| `Day2/Day2_DeepDive_Regression.md` | `units/unit_01_foundations/deep_dive_regression.md` | Student Unit 1 |
| `Day2/Day2_DeepDive_Unsupervised.md` | `units/unit_02_classical_ml/deep_dive_unsupervised.md` | Student Unit 2 |
| `Day2/Day2_Master_Agenda.md` | `instructor_resources/lesson_plans/Day_02_Primer.md` | Instructor (Local) |
| `Day2/Day2_Master_ML_Theory_Primer.md` | `units/unit_01_foundations/ml_theory_primer.md` | Student Unit 1 |
| `Day2/assets/*.png` | `units/unit_01_foundations/assets/` | Unit 1 Assets |

---

## 7. Implementation Roadmap

1. **Phase 1 (Scaffolding & Isolation):**
   * Configure `.gitignore` (ignoring `instructor_resources/`) and `.pre-commit-config.yaml` (`nbstripout`).
   * Create directory structure: `units/`, `labs/`, `datasets/`, `assessments/`, `supplementary_resources/`, and `instructor_resources/`.
   * Add `instructor_resources/templates/session_log_template.md`.
2. **Phase 2 (Migration):**
   * Relocate Day 1 and Day 2 files according to the Section 6 migration table.
   * Generate `SCHEDULE.md` linking Day 1 through Day 24 to corresponding units and labs.
3. **Phase 3 (Next Curriculum Deliverables):**
   * Complete Unit 1.2 (*Data Preprocessing & Sequence Encoding*) notebook and Lab 01 (*Gene Expression Preprocessing*).
