# Unit 1: Foundations of Machine Learning for Bioinformatics

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  

---

## Unit Overview

Machine learning models cannot directly interpret raw biological sequences or files. DNA sequences (`A, C, T, G`), RNA transcript counts, and mass spectrometry measurements must first be structured, scaled, and transformed into numerical matrices.

In this foundational unit, you will learn the core paradigms of machine learning (supervised vs. unsupervised), master biological data preprocessing and feature representation ($k$-mers, one-hot encoding, missing value imputation), and build regression models to predict continuous biological outcomes such as epigenetic biological age and gene expression levels.

---

## Core Topics & Syllabus Breakdown

### 1.1 Introduction to Machine Learning in Bioinformatics
* **Machine Learning in Biology:** Traditional rule-based bioinformatic algorithms vs. data-driven statistical learning.
* **Supervised Learning:** Learning a function $f(X) \to y$ from ground-truth labeled biological datasets (e.g., tumor vs. normal expression profiles).
* **Unsupervised Learning:** Discovering patterns, clusters, and latent structures in unlabeled biological matrices (e.g., single-cell clustering, novel pathogen discovery).
* **Core Biological Tasks:**
  * *Classification Task:* Distinguishing tumor phenotypes (benign vs. malignant) from molecular biomarker levels.
  * *Regression Task:* Predicting continuous outcomes such as patient biological age from DNA methylation profiles.
  * *Clustering Task:* Grouping patient gene expression profiles into molecular subtypes without prior disease labels.

### 1.2 Data Preprocessing & Biological Feature Engineering
* **Handling Missing Values:** Biological zeros vs. technical dropout; mean/median vs. $k$-Nearest Neighbor (KNN) imputation.
* **Normalization & Scaling:** Feature scaling principles; Min-Max scaling, Z-score standardization, and RNA-seq library size normalization ($\log_2(\text{CPM} + 1)$).
* **Sequence Representation & Encoding:**
  * **One-Hot Encoding:** Converting nucleotide characters into 4-dimensional binary vectors ($A=[1,0,0,0]^T$, $C=[0,1,0,0]^T$, etc.).
  * **$k$-mer Counting:** Splitting DNA and protein sequences into overlapping substrings of length $k$ to construct frequency vectors for alignment-free analysis.

### 1.3 Supervised Learning — Regression
* **Linear & Polynomial Regression:** Formulating $y = \mathbf{w}^T \mathbf{x} + b$; Ordinary Least Squares (OLS) and gradient descent optimization.
* **Overfitting & Regularization:** Managing high-dimensional genomic data ($p \gg n$); L1 Lasso (sparse feature selection) and L2 Ridge (weight shrinkage).
* **Evaluation Metrics for Continuous Outputs:**
  * Mean Squared Error ($\text{MSE}$) and Root Mean Squared Error ($\text{RMSE}$)
  * Mean Absolute Error ($\text{MAE}$)
  * Coefficient of Determination ($R^2$ score)

### 1.4 Biological Data Regression Applications
* **Predicting Epigenetic Age:** Using DNA methylation CpG site beta values to estimate chronological and biological age.
* **Gene Expression Dose-Response:** Modeling the continuous expression level of target oncogenes as a function of pharmaceutical inhibitor dosage.

---

## Folder Contents & Materials

| File / Resource | Type | Description |
|---|---|---|
| [1.1_intro_ml_in_bioinformatics.ipynb](1.1_intro_ml_in_bioinformatics.ipynb) | Jupyter Notebook | Interactive introduction to biological datasets, feature matrices, and target vectors. |
| [problem_formulation_tool.ipynb](problem_formulation_tool.ipynb) | Interactive Tool | Guided questionnaire to formulate biological research questions into machine learning tasks. |
| [ml_theory_primer.md](ml_theory_primer.md) | Theory Guide | Comprehensive foundations, vocabulary definitions, and mathematical formulations. |
| [deep_dive_regression.md](deep_dive_regression.md) | Technical Guide | Mathematical formulation of OLS, cost surfaces, gradient descent, and regularized regression. |
| [career_perspectives.md](../../supplementary_resources/career_perspectives.md) | Industry Guide | Career pathways across Biopharma, Clinical Diagnostics, and Computational Biology. |
| [assets/](assets/) | Visual Diagrams | Reference infographics illustrating classification, clustering, regression, and ML taxonomy. |

---

## Associated Laboratory Practicals

* **[Lab 01](../../labs/lab_01_expression_preprocessing/):** RNA-seq Gene Expression Preprocessing, Log-transformation, and Quantile Normalization.
* **[Lab 02](../../labs/lab_02_biological_regression/):** Epigenetic Aging Clock: Training and Regularizing a Continuous Regression Model.

---

## Suggested Study Plan

1. Read [ml_theory_primer.md](ml_theory_primer.md) for fundamental terminology and concepts.
2. Complete [problem_formulation_tool.ipynb](problem_formulation_tool.ipynb) to practice identifying ML task types from biological scenarios.
3. Run and experiment with the code in [1.1_intro_ml_in_bioinformatics.ipynb](1.1_intro_ml_in_bioinformatics.ipynb).
4. Review [deep_dive_regression.md](deep_dive_regression.md) before starting Lab 01 and Lab 02.
