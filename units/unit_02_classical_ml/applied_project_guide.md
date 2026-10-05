---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Classical ML Applied Project
document_type: Project Blueprint & Dataset Guide
ai_tier: "Tier 4: Full AI + Reflection"
---

# Applied ML Project: Dataset Selection & Pipeline Blueprint

**Course Code:** `02BMSBI24365` — AI and ML in Bioinformatics  
**Overview:** This guide outlines the requirements for selecting a biological dataset and details the 8 mandatory stages required to complete an End-to-End Machine Learning Bioinformatics Pipeline. This project compiles your learnings from Units 1 and 2. Use this guide to prepare your Project Milestone 1 Charter submission.

---

## 1. The 8-Stage End-to-End Bioinformatics Pipeline
To successfully complete your applied project, your team must execute and document these 8 sequential stages. Use this as the structural blueprint for your project notebook.

1. **Biological Problem & Hypothesis Formulation:** Clearly define your clinical, genomic, proteomic, or pharmacological objective.
2. **Data Acquisition & Hygiene:** Secure data from reputable sources (e.g., NCBI GEO, TCGA, UCI, Kaggle). Ensure `.gitignore` compliance (never commit raw biological data to GitHub).
3. **Exploratory Data Analysis (EDA) & Quality Control:** Evaluate missingness, detect outliers, identify skewness, and measure target class balance.
4. **Preprocessing & Leak-Free Transformation:** Use Scikit-learn `Pipeline` to encapsulate imputation, scaling (`StandardScaler`, `RobustScaler`), and categorical encoding securely.
5. **Dimensionality Reduction & Feature Selection:** Apply variance thresholding, `SelectKBest`, or PCA (vital if you have high-dimensional genomic sets where $p \gg n$).
6. **Model Training & Comparison Suite:** Benchmark a baseline Linear/Logistic model against an ensemble tree (Decision Tree, Random Forest) and an Artificial Neural Network (ANN) baseline.
7. **Diagnostic Metric Evaluation:** Produce a Confusion Matrix, ROC-AUC, and PR Curves for classification, or calculate $R^2$ and MAE/RMSE for regression. Always use Stratified Cross-Validation.
8. **Explainable AI & Biological Discovery:** Extract feature importances (e.g., using SHAP) to identify top driver genes or clinical markers, and explain the final biological meaning of the model.

---

## 2. Dataset Feasibility Vetting Rubric (Self-Check Guide)
Before submitting your Project Charter, evaluate your proposed dataset using this checklist. The instructor will use these exact criteria to approve or reject your dataset.

### A. Sample Size Feasibility ($n$)
* 🟢 **Safe Zone:** $100 \le n \le 5,000$. Ideal for classical machine learning and rapid iteration on personal hardware.
* 🔴 **Red Flag 1 (Too Small):** $n < 40$. Inadequate sample size for cross-validation; extreme risk of high-variance over-fitting.
* 🔴 **Red Flag 2 (Too Large):** $n > 500,000$ tabular rows, or raw gigapixel image sets without preprocessing. This will overwhelm local hardware and Conda memory.

### B. Dimensionality ($p$) & Curse of Dimensionality ($p \gg n$)
* 🟢 **Ideal Tabular:** $5 \le p \le 100$. Clean, interpretable features (e.g., clinical vital signs, targeted biomarker panels).
* 🟡 **High-Dimensional Genomic:** $p = 20,000$ (e.g., Whole-transcriptome RNA-seq). Permitted **only if** you explicitly define a feature-reduction strategy (e.g., extracting the top 1,000 highly variable genes (HVGs), `SelectKBest`, or PCA) inside your ML `Pipeline`.

### C. Target Label Definition ($y$)
* You must have an unambiguous, pre-defined ground truth in the dataset.
* **Binary Classification:** Clearly defined biological states (e.g., Pathogenic vs. Benign, Sensitive vs. Resistant).
* **Continuous Regression:** Continuous physical/clinical units (e.g., survival in months, biomarker concentration in $ng/mL$).
* 🔴 **Red Flag:** Datasets lacking ground-truth targets altogether (pure clustering tasks are not permitted for this applied project without specific instructor approval).

### D. Data Hygiene & Preprocessing Traps
* **Biologically Impossible Values:** Check for clinical metrics like blood pressure or BMI recorded as `0.0`—these usually represent missing values disguised as numbers.
* **Target Leakage:** Does any column implicitly contain the answer (e.g., a `biopsy_performed_flag` or `patient_discharge_date`)?

---

## 3. Dataset Assessment Examples
Review these examples of evaluated datasets to understand how to correctly scope your project proposal parameters.

| Biological Domain & Clinical Question | Proposed Dataset | Sample Size ($n$) | Features ($p$) | Task Formulation | Target Variable ($y$) | Vetting Status |
|---|---|---|---|---|---|---|
| Breast Cancer Recurrence Prediction | GEO GSE2034 | $n = 286$ | $p = 100$ genes | Binary Classification | Recurrent vs. Disease-Free | 🟢 **Approved:** Ensure stratified split due to class imbalance (~20% recurrent). |
| Chemotherapy Drug Sensitivity ($IC_{50}$) | Genomics of Drug Sensitivity in Cancer | $n = 800$ cell lines | $p = 500$ drivers | Continuous Regression | $\log(IC_{50})$ value ($\mu\text{M}$) | 🟡 **Needs Pruning:** $p$ is too large for sample size; requires PCA pipeline. |
| Heart Disease Risk Stratification | Kaggle / UCI Heart Disease | $n = 303$ | $p = 13$ metrics | Binary Classification | Diagnosis ($>50\%$ stenosis) | 🟢 **Approved:** Emphasize feature scaling (`RobustScaler`). |
| Alzheimer's Progression Biomarkers | ADNI / GEO GSE63060 | $n = 249$ | $p = 19,000$ probes | Multi-Class Classification | Control vs. MCI vs. AD | 🟡 **Scoping:** Reduce to top 500 variance genes or apply PCA first. |
| Pima Indians Diabetes Onset | UCI ML Repository | $n = 768$ | $p = 8$ clinical features | Binary Classification | Diabetic onset | 🟢 **Approved:** Beware of biologically impossible `0`s in insulin, impute as NaN. |

---

## 4. Curated Repository Catalog (Dataset Recommendations)
If you have not yet selected a dataset, or if your initial dataset does not meet the rubric criteria, please explore these verified repositories:

### A. Course Internal Benchmark Repositories ([datasets/README.md](../../datasets/README.md))
* **Wisconsin Diagnostic Breast Cancer (WDBC):** $n = 569, p = 30$. Excellent baseline for comparative classification, feature selection, and ROC-AUC analysis.
* **Epigenetic Aging Clock (GSE40279):** $n = 650, p = 500$ CpG beta values. Ideal for continuous Ridge/Lasso regression and polynomial modeling.
* **Serum Proteomics Mass Spectrometry:** $n = 216, p = 100$ peak features. Superb for multi-class staging and PCA dimensionality reduction.

### B. NCBI Gene Expression Omnibus (GEO)
* Search for **"Series Matrix"** files (`.txt.gz`).
* *Recommended accession examples:*
  * `GSE2034`: Breast cancer relapse prediction ($n = 286$).
  * `GSE19804`: Lung cancer in non-smokers ($n = 120$).
  * `GSE42832`: Peripheral blood diagnostic panel for Rheumatoid Arthritis ($n = 200$).

### C. UCI Machine Learning Repository — Biology & Health
* **Heart Disease Cleveland Database** ($n = 303, p = 14$).
* **Chronic Kidney Disease** ($n = 400, p = 24$, mixed categorical/numerical).
* **Parkinson’s Disease Biomedical Voice Measurements** ($n = 195, p = 22$).

### D. Kaggle Biomedical & Clinical Datasets
* **Pima Indians Diabetes Database** ($n = 768, p = 8$).
* **Stroke Prediction Dataset** ($n = 5,110, p = 11$, classic severe class imbalance challenge).
* **Hepatitis C Clinical Biomarkers** ($n = 615, p = 13$).

### E. The Cancer Genome Atlas (TCGA) via cBioPortal
* You can download pre-cleaned clinical and mRNA expression matrices across 33 cancer types (e.g., TCGA-BRCA, TCGA-LUAD, TCGA-GBM) with beautifully annotated patient survival data directly from the cBioPortal interface.