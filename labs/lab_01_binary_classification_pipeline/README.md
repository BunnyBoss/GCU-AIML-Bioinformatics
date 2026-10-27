---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
document_type: Laboratory Practical Guide
ai_tier: "Tier 3: AI Collaboration (Disclosed)"
---

# Lab Exercise 01: End-to-End Binary Classification Pipeline for Gene Expression

**Course Code:** `02BMSBI24365` — AI and ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  
**Assigned AI Tier:** Tier 3: AI Collaboration (Disclosed)  
**Session Agendas:** [Day 16 Student Agenda](day_16_student_agenda.md) | [Day 17 Student Agenda](day_17_student_agenda.md)  
**Primary Deliverable:** Executable Jupyter Notebook (`lab_01_binary_classification_pipeline.ipynb`)  
**Submission Channel:** Course GitHub Repository via **GitHub Issues** (Milestone / Lab Exercise 1 Submission)

---

## 1. Clinical Context & Biological Problem Statement

Breast cancer is not a single homogeneous disease; it represents a biologically diverse collection of molecular entities with distinct transcriptomic profiles, clinical trajectories, and therapeutic responses. Under the landmark **Perou-Sørlie PAM50 classification system**, two of the most critical and divergent intrinsic subtypes are:

1. **Luminal A (`BRCA_LumA`):**
   * **Molecular Hallmarks:** High expression of Estrogen Receptor (*ESR1*), Progesterone Receptor (*PGR*), and luminal transcription factors (*GATA3*, *FOXA1*); low expression of cell proliferation markers (*MKI67*).
   * **Clinical Course:** Favorable 10-year overall survival; highly responsive to endocrine/hormone therapy (Tamoxifen, Aromatase Inhibitors); typically spares patients cytotoxic chemotherapy.
2. **Basal-like (`BRCA_Basal`):**
   * **Molecular Hallmarks:** Absence of hormone receptor expression (ER-/PR-/HER2- phenotype, overlapping heavily with Triple-Negative Breast Cancer [TNBC]); pronounced overexpression of basal cytokeratins (*KRT5*, *KRT14*, *KRT17*), *EGFR*, and aggressive mitotic/proliferation drivers (*MKI67*, *CCNB1*, *FOXC1*).
   * **Clinical Course:** Aggressive clinical course, early recurrence, visceral metastasis, and lack of targeted endocrine vulnerabilities. Demands immediate systemic cytotoxic chemotherapy.

### The Clinical Asymmetry of Misclassification
In oncology decision support, not all errors are equal:
* **False Negative (FN) [Missing a Basal tumor as Luminal A]:** Catastrophic. A patient with an aggressive, highly proliferative tumor is misdiagnosed as having low-risk disease, missing critical cytotoxic chemotherapy and leading to metastatic progression.
* **False Positive (FP) [Flagging a Luminal A tumor as Basal-like]:** Suboptimal. Causes heightened psychological stress and subjects a patient to intensive chemotherapy evaluation, but secondary immunohistochemical (IHC) testing provides a safety net.

**Core Objective:** We will construct a leak-free, reproducible machine learning and deep learning classification suite that accurately stratifies primary breast tumors while establishing a calibrated clinical decision threshold ($\tau$) designed to drive False Negatives toward zero.

---

## 2. Dataset Schema & Molecular Profile

The benchmark cohort is sourced directly from **The Cancer Genome Atlas (TCGA) Breast Invasive Carcinoma PanCancer Atlas cohort** via the cBioPortal data repository.

* **Cohort File:** `data/tcga_brca_expression.csv` (mirror available at `datasets/raw/tcga_brca_expression.csv`)
* **Cohort Dimensions:** 670 primary tumor patient biopsies $\times$ 60 curated genes.
* **Target Label Distribution:**
  * `0 = BRCA_LumA` (Luminal A, ER+): 499 patients ($74.5\%$)
  * `1 = BRCA_Basal` (Basal-like, TNBC-like): 171 patients ($25.5\%$)

| Column Name | Data Type | Units / Range | Description |
|---|---|---|---|
| `sample_id` | String | TCGA Aliquot ID | Unique biospecimen identifier (e.g., `TCGA-3C-AAAU-01`). |
| `patient_id` | String | TCGA Participant ID | Patient registry code (e.g., `TCGA-3C-AAAU`). |
| `subtype` | String | Categorical | Verified PAM50 subtype (`BRCA_LumA` vs. `BRCA_Basal`). |
| `target` | Integer | `0` or `1` | Ground-truth binary target (`1 = BRCA_Basal`, `0 = BRCA_LumA`). |
| *Gene Columns (60)* | Float | Batch-normalized RSEM | Normalized RNA-seq transcript abundance across PAM50 signature genes and key oncogenic drivers (*ESR1*, *PGR*, *ERBB2*, *KRT5*, *KRT14*, *GATA3*, *MKI67*, *EGFR*, etc.). |

---

## 3. Data Acquisition & Preprocessing Architecture

Students and instructors have two pathways to work with the data:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                         TWO PATHWAYS FOR COHORT INGESTION                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                        │
│ PATHWAY A: Quick Start (Default for Lab Session)                                       │
│    Directly load `data/tcga_brca_expression.csv` inside the Jupyter Notebook.          │
│    Zero download or processing latency (<0.05 seconds).                                │
│                                                                                        │
│ PATHWAY B: End-to-End Raw ETL Pipeline (Full Traceability)                             │
│    1. Download raw cBioPortal files (clinical + 147 MB RSEM matrix):                   │
│       bash datasets/download_scripts/download_data.sh                                  │
│    2. Run the lab preprocessing script to assemble the CSV:                            │
│       python labs/lab_01_binary_classification_pipeline/preprocess_raw_tcga.py         │
│                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### The Preprocessing Script (`preprocess_raw_tcga.py`)
Located directly in this lab directory, `preprocess_raw_tcga.py` documents and automates how the raw data is prepared:
1. **Clinical Ingestion:** Reads `data_clinical_patient.txt` and `data_clinical_sample.txt` from `datasets/raw/`.
2. **Subtype Filtering:** Filters for primary tumors (`SAMPLE_TYPE == "Primary"`) annotated as `BRCA_LumA` or `BRCA_Basal`, keeping one unique biopsy per patient (670 patients total).
3. **Expression Slicing:** Extracts the 60 canonical PAM50 and oncogenic driver genes from the 20,531 genes in `data_mrna_seq_v2_rsem.txt`.
4. **Cohort Export:** Transposes the expression matrix (patients as rows, genes as columns) and outputs `data/tcga_brca_expression.csv`.

```bash
# To re-generate the dataset from raw cBioPortal files at any time:
python labs/lab_01_binary_classification_pipeline/preprocess_raw_tcga.py
```

---

## 4. The 10-Stage Sequential Pipeline Architecture

The practical notebook organizes the classification workflow into sequential, self-contained sections:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      10-STAGE SEQUENTIAL PIPELINE ARCHITECTURE                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Stage 1: Biological Problem Formulation & Clinical Stakes                              │
│ Stage 2: Raw Data Ingestion & Quality Control Audit                                    │
│ Stage 3: Exploratory Data Analysis (EDA) & 2D PCA Projection                           │
│ Stage 4: Leak-Free Preprocessing & Stratified Cohort Partitioning                      │
│ Stage 5: Statistical Biomarker Ranking (ANOVA F-Score)                                 │
│ Stage 6: Model 1 — Logistic Regression (Train → Test → Metrics → Odds Ratios)          │
│ Stage 7: Model 2 — Random Forest Classifier (Train → Test → Metrics → Gini Importance) │
│ Stage 8: Model 3 — Keras ANN (Architecture → Train → Metrics → Threshold Tuning τ)     │
│ Stage 9: Multi-Model Benchmark Synthesis & Combined ROC Curves                         │
│ Stage 10: Biological Synthesis & Point-of-Care 5-Gene Diagnostic Panel                 │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Model Suite & Benchmark Requirements

Every student must implement, calibrate, and compare three complementary model families on the exact same train/test splits:

1. **L2-Regularized Logistic Regression:**
   * Serves as the interpretable linear baseline.
   * Extraction of standardized model coefficients and Odds Ratios ($\text{OR} = e^{w_j}$) to measure relative gene expression risk.
2. **Random Forest Classifier (Ensemble):**
   * Captures non-linear biological epistatic interactions across gene combinations.
   * Evaluation of Gini Feature Importance (Mean Decrease in Impurity) to rank the top 10 biomarker drivers.
3. **Artificial Neural Network (Keras / TensorFlow MLP):**
   * Deep learning representation connecting Units 3.1 & 3.2.
   * Input ($p$ features) $\to$ `Dense(32, activation='relu')` $\to$ `Dropout(0.30)` $\to$ `Dense(16, activation='relu')` $\to$ `Dense(1, activation='sigmoid')`.
   * Compilation: `optimizer='adam'`, `loss='binary_crossentropy'`.
   * Tracking training vs. validation loss trajectories over 50 epochs ($B=32$) to monitor for overfitting in $p \gg n$ regime.

---

## 6. Submission & Evaluation Rubric

### Submission Protocol via GitHub Issues
1. Complete all code cells, markdown reflections, and diagnostic visualizations inside `lab_01_binary_classification_pipeline.ipynb`.
2. Clear large execution blobs using `nbstripout` (`pre-commit run --all-files`).
3. Open a **New Issue** on the course GitHub repository titled:  
   `[Lab Exercise 01 Submission] - <Team Name or Student Name> - <Cohort/Dataset>`
4. Post your summary report containing:
   * A table comparing test metrics across the three models (Accuracy, Sensitivity, Specificity, Precision, F1, ROC-AUC).
   * A screenshot or markdown embed of your combined ROC curve and optimal threshold ($\tau$) plot.
   * A 3-sentence biological interpretation linking your top identified gene biomarkers to published cancer biology literature.
   * AI Collaboration Disclosure statement detailing how AI was utilized for debugging, brainstorming, or drafting code.

### Grading Rubric (100 Points Total)

| Evaluation Category | Points | Criteria |
|---|---|---|
| **Data Hygiene & Leak-Free Rigor** | 20 | Explicit stratified train/test split; strict zero-leakage invariant (`StandardScaler` fitted *only* on training data; no global transformations). |
| **Model Implementation & Tuning** | 25 | All 3 models (Logistic Regression, Random Forest, Keras ANN) correctly instantiated, trained, and tuned on identical splits. |
| **Diagnostic Metrics & Visualizations** | 25 | Side-by-side Confusion Matrices, multi-model ROC-AUC curve overlay, Precision-Recall curves, and calibrated threshold tuning ($\tau$). |
| **Biomarker Extraction & Biology** | 15 | Clear biological discussion of top drivers (*ESR1*, *GATA3*, *KRT5*, *EGFR*, etc.) with correct clinical directionality. |
| **Student Extension & AI Reflection** | 15 | Completed independent challenge extension and clear AI tool disclosure audit. |
