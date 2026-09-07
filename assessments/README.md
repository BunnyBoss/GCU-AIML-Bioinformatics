# Assessments & Evaluation Framework

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Program:** M.Sc. Bioinformatics (Semester III)  
**Evaluation Model:** Continuous Internal Assessment (CIA) + End-Semester Examination (ESE)  

---

## Evaluation Architecture & Marks Weightage

The evaluation for `02BMSBI24365` is divided into Continuous Internal Assessment (50%) and the University End-Semester Examination (50%):

| Component | Weightage | Description | Schedule |
|---|---|---|---|
| **Diagnostic Baseline Quiz** | Diagnostic (0%) | Non-graded readiness assessment covering Python, Git, linear algebra, and molecular biology basics. | Week 1 |
| **Continuous Internal Quizzes (2x)** | 15% | Two periodic assessments testing conceptual theory, mathematical intuition, and algorithmic trade-offs. | Week 4 & Week 8 |
| **Laboratory Practicals & Code Hygiene** | 20% | Graded lab notebooks (Labs 01–09), code reproducibility, and challenge problem solutions. | Weekly |
| **Capstone Project (Lab 10)** | 15% | End-to-end multi-omics machine learning project with technical report, code repository, and viva voce. | Weeks 11–12 |
| **End-Semester Examination (ESE)** | 50% | Comprehensive theoretical and computational examination. | End of Semester |

---

## Folder Contents

* [diagnostic_baseline_quiz.md](diagnostic_baseline_quiz.md): 10-question diagnostic quiz administered during Week 1 to assess prerequisite comfort across programming, mathematics, and molecular biology.

---

## Laboratory Practical Evaluation Rubric (Per Lab: 10 Marks)

Each laboratory assignment is evaluated across four core criteria:

| Criterion | Marks | Evaluation Standard |
|---|---|---|
| **Data Handling & Preprocessing** | 2.5 | Proper handling of missing values, correct biological scaling/normalization, and zero data leakage across train/test splits. |
| **Model Implementation & Tuning** | 2.5 | Correct algorithm selection, appropriate hyperparameter choices, and clean execution using Scikit-learn / TensorFlow. |
| **Validation & Diagnostic Metrics** | 2.5 | Thorough evaluation using appropriate metrics (ROC-AUC, Precision-Recall, Confusion Matrix, $R^2$), with clear interpretation of biological consequences. |
| **Student Challenge & Insights** | 2.5 | Successful completion of the unguided challenge problem; clear scientific commentary explaining the biological implications of the model's output. |

---

## Capstone Project Guidelines (Lab 10)

The Capstone Mini-Project allows you to synthesize the entire curriculum by tackling a real-world translational biology challenge:
1. **Approved Domains:**
   * Multi-omics cancer subtype discovery and survival prognosis.
   * Pathogenicity prediction of non-coding genomic variants.
   * Automated histopathology image classification with attention-map localization.
   * Explainable drug response prediction across cancer cell line panels (GDSC / CCLE).
2. **Mandatory Deliverables:**
   * Fully reproducible GitHub repository with documented virtual environment (`environment.yml`).
   * Clean Jupyter notebook with zero data leakage, cross-validation, and baseline model comparison.
   * **Explainable AI (XAI) Audit:** Demonstration of SHAP or attention-based feature attribution validating top predictive biomarkers against existing biological literature.
   * 4-page written report following standard scientific manuscript format (Abstract, Introduction, Methods, Results, Discussion).
