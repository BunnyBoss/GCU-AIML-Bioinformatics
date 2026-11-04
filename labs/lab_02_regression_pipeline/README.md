---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
document_type: Laboratory Practical Guide
ai_tier: "Tier 3: AI Collaboration (Disclosed)"
---

# Lab Exercise 02: End-to-End Regression Pipeline & Continuous Disease Progression

**Course Code:** `02BMSBI24365` — AI and ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  
**Assigned AI Tier:** Tier 3: AI Collaboration (Disclosed)  
**Session Agenda:** [Day 19 Student Agenda](day_19_student_agenda.md)  
**Primary Deliverable:** Executable Jupyter Notebook (`lab_02_regression_pipeline.ipynb`)  
**Submission Channel:** Course GitHub Repository via **GitHub Issues** (Milestone / Lab Exercise 2 Submission)

---

## 1. Clinical Context & Biological Problem Statement

While diagnostic classification answers discrete categorical questions (e.g., *Is this tumor malignant or benign?*), many vital clinical and biological questions demand continuous numerical prediction:
* *What is the patient's quantitative disease progression score one year following baseline diagnosis?*
* *What is the minimum effective drug concentration ($IC_{50}$) required to inhibit viral replication?*
* *What is the biological aging delta derived from epigenetic DNA methylation clocks?*

### The Clinical Cost of Continuous Prediction Errors
In regression, prediction errors are continuous residuals: $e_i = y_i - \hat{y}_i$.
* **Symmetric vs. Asymmetric Errors:** Overestimating disease severity may cause unnecessary aggressive medication changes with toxic side effects; underestimating progression risks delayed clinical intervention.
* **Large Miss Penalties:** In therapeutic dosing and risk assessment, small errors are clinically tolerable, but catastrophic misses can prove fatal. This distinction underpins why we evaluate both linear ($L_1$, MAE) and squared ($L_2$, RMSE) metrics.

**Core Objective:** We will construct a leak-free, reproducible machine learning regression pipeline that takes raw clinical features, audits data quality, performs exploratory data analysis, trains a triad of complementary regression models (Ridge, Random Forest, Gradient Boosting), and validates performance using continuous evaluation metrics and residual diagnostics.

---

## 2. Dataset Schema & Feature Dictionary

The raw clinical cohort is located at `datasets/raw/lab_02_day_19_diabetes_regression_raw.csv` and contains records from $n = 442$ patient baseline examinations with 10 physiological and biochemical measurements.

| Column Name | Data Type | Natural Units / Range | Clinical Description |
|---|---|---|---|
| `patient_id` | String | `PAT_001` to `PAT_442` | Unique patient registry identifier. |
| `age` | Float | 19 – 79 years | Patient chronological age at baseline examination. |
| `sex` | Float | 1.0 (Female), 2.0 (Male) | Biological sex indicator. |
| `bmi` | Float | 18.0 – 42.2 $\text{kg/m}^2$ | Body Mass Index (weight in kg / height in $\text{m}^2$). |
| `bp` | Float | 62.0 – 133.0 mmHg | Mean arterial blood pressure. |
| `s1_tc` | Float | 97.0 – 301.0 mg/dL | Total serum cholesterol level. |
| `s2_ldl` | Float | 59.6 – 242.4 mg/dL | Low-density lipoproteins ("bad" cholesterol). |
| `s3_hdl` | Float | 19.0 – 99.0 mg/dL | High-density lipoproteins ("good" cholesterol). |
| `s4_tch` | Float | 2.0 – 9.09 | Total cholesterol / HDL ratio (atherogenic index). |
| `s5_ltg` | Float | 3.61 – 6.11 | Logarithm of serum triglycerides concentration. |
| `s6_glu` | Float | 58.0 – 124.0 mg/dL | Fasting blood glucose concentration. |
| `target` | Float | 25.0 – 346.0 | Quantitative disease progression index recorded 1 year after baseline. |

---

## 3. Data Acquisition & Data Quality Pass

The raw data file is generated via the reproducible automation script in `datasets/download_scripts/`:

```bash
# To generate or re-create the raw data file at any time:
python datasets/download_scripts/download_lab_02_regression_data.py
```

### Realistic Data Quality Challenges Injected:
To emulate real-world electronic health record (EHR) data, the raw table deliberately includes:
1. **Duplicate Patient Records:** Multiple duplicate rows that must be identified and removed via `df.duplicated()`.
2. **Missing Observations (`NaN`):** Randomly missing values across `bmi`, `bp`, and `s6_glu` requiring median imputation.
3. **Invalid Clinical Anomalies:** Negative age entries (e.g., `-99.0`) and non-physiological readings (e.g., `bmi = -5.0`, `bp = 0.0`) that must be audited and filtered before statistical modeling.

---

## 4. The 9-Stage Sequential Pipeline Architecture

The practical notebook organizes the regression workflow into sequential, self-contained stages:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      9-STAGE SEQUENTIAL PIPELINE ARCHITECTURE                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Stage 1: Clinical Problem Formulation & Continuous Prediction Stakes                   │
│ Stage 2: Raw Ingestion & Initial Data Audit                                            │
│ Stage 3: Data Quality Pass (Deduplication, Anomaly Filtering, Median Imputation)       │
│ Stage 4: Exploratory Data Analysis (EDA, Target Skewness, Correlation Heatmap)         │
│ Stage 5: Leak-Free Preprocessing & Train/Test Partitioning                             │
│ Stage 6: Model 1 — Regularized Linear Regression (Ridge Baseline & Biomarker Weights)  │
│ Stage 7: Model 2 — Random Forest Regressor (Ensemble Trees & Feature Importances)      │
│ Stage 8: Model 3 — Gradient Boosting Regressor (Sequential Residual Minimization)      │
│ Stage 9: Multi-Model Benchmark Synthesis & Comparative Performance Analysis            │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Continuous Evaluation Metrics

Unlike classification, accuracy and confusion matrices do not apply to continuous quantities. We evaluate models using three complementary continuous metrics:

1. **Mean Absolute Error (MAE):**
   $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
   Measures the average magnitude of clinical prediction error in original disease progression units. Robust to outliers.
2. **Root Mean Squared Error (RMSE):**
   $$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
   Assigns quadratic penalties to errors, highlighting large discrepancies between predicted and true patient trajectories.
3. **Coefficient of Determination ($R^2$):**
   $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
   Measures the proportion of variance in disease progression explained by our clinical predictors relative to a naive model predicting the sample mean $\bar{y}$.

---

## 6. Model Suite & Benchmark Requirements

Every student must implement, train, and compare three model families on the exact same train/test splits:

1. **L2-Regularized Linear Regression (Ridge):**
   * Configured with $\alpha = 1.0$ to stabilize collinear lipid features (`s1_tc` vs. `s2_ldl`).
   * Standardized regression coefficients ($\mathbf{w}$) show directional risk (e.g. positive risk for `s5_ltg` and `bmi`; negative protective weight for `s3_hdl`).
2. **Random Forest Regressor:**
   * 100-tree ensemble with `max_depth = 6` and `min_samples_split = 5` to constrain variance on small cohorts.
   * Ranks features via Mean Decrease in Impurity (Gini importance).
3. **Gradient Boosting Regressor:**
   * Sequential boosting with `n_estimators = 100`, shallow base trees (`max_depth = 3`), and shrinkage (`learning_rate = 0.05`).
   * Iteratively corrects residual errors left unexplained by previous trees.

---

## 7. Submission & Evaluation Rubric

### Group Repository Structure & Submission Protocol

Submissions for Lab Exercise 02 are completed in collaborative student groups. Each group maintains a dedicated, lightweight GitHub practicals repository and submits their work via the main course repository:

#### 1. Group Practicals Repository Setup
Each student creates and maintains their own personal practicals repository (e.g. `gcu-aiml-labs`). Inside that repository, structure the directory as:
```text
gcu-aiml-labs/
└── lab_02_regression/
    ├── download_lab_02_regression_data.py
    └── lab_02_regression_pipeline.ipynb
```
> ⚠️ **Preserve Cell Execution Outputs:** Execute all notebook cells end-to-end and **save the notebook with all outputs (plots, correlation heatmaps, metric summaries) intact**. Do not strip execution outputs; instructors require fully rendered visual outputs for assessment and grading.

#### 2. Single Designated Group Submitter
To avoid duplicate submission tickets, **only ONE designated member from each group** opens the submission Issue on the main course repository on behalf of their entire team:
* **Issue Title:** `[Lab 02 Submission] Group <Number/Name> — Regression Pipeline & Progression Prediction`
* **Issue Body Template:**
```markdown
### Group Information
* **Group Name / Number:** Group 3 — OncoPredict
* **Group Members:**
  1. Jane Doe (Reg No: 24MSBI001) [Designated Submitter]
  2. John Smith (Reg No: 24MSBI005)
  3. Alice Johnson (Reg No: 24MSBI012)
* **Repository / Folder Link:** https://github.com/<username>/gcu-aiml-labs/tree/main/lab_02_regression

### 1. Model Benchmark Comparison
| Model Architecture | Model Type | Train R² | Test R² | Test MAE | Test RMSE |
|---|---|---|---|---|---|
| Ridge Regression (alpha=1.0) | Linear (L2 Regularized) | 0.5375 | 0.3706 | 43.05 | 52.97 |
| Random Forest (100 Trees) | Ensemble (Parallel Bagging) | 0.7979 | 0.2924 | 46.07 | 56.16 |
| Gradient Boosting (100 Trees) | Ensemble (Sequential Boosting) | 0.7666 | 0.2855 | 46.32 | 56.44 |

### 2. Clinical & Methodological Interpretation (3 Sentences)
1. Baseline Body Mass Index (BMI) and serum triglycerides (s5_ltg) represent the primary positive drivers of accelerated 1-year disease progression, whereas high-density lipoproteins (s3_hdl) confer a protective negative association.
2. Regularized Ridge regression achieved the highest generalization performance on unseen patient test data (Test R² = 0.3706), outperforming both non-linear tree ensembles.
3. On modest clinical sample sizes (n ~ 400) with predominantly additive physiological risk factors, complex tree ensembles overfit training variations, illustrating the Occam's Razor principle in biomedical machine learning.
```

#### 3. Individual Member Portfolios
While only one student submits the ticket on behalf of the group, **all group members must commit and maintain a copy of the executed notebook and data script in their own personal GitHub repositories** for their individual records and academic portfolios.
