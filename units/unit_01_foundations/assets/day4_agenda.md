---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 1 — Foundations of Machine Learning for Bioinformatics
document_type: Session Agenda
ai_tier: Full AI (Learning Aid)
---

# 📅 Day 4 Agenda: Data Transformations & Feature Engineering (Part B)

Welcome to Session 4. Today, we will expand our data preprocessing toolkit from structural cleaning into numerical data transformations, learning how to scale, center, and stabilize feature distributions across clinical and genomic datasets.

---

## 1. Recap & Errata
* **Immediate Recap (Day 03):** A review of the four foundational data-cleaning steps covered in Part A:
  * Handling missing values with imputation (`SimpleImputer`).
  * Removing constant, zero-variance features (`VarianceThreshold`).
  * Eliminating duplicate records.
  * Converting categorical metadata into numerical arrays via One-Hot Encoding (`pd.get_dummies`).
* **Clarification (Rollover from Day 02):** Addressing the visual vs. analytical y-intercept in the Day 2 regression visualization from [1.1_intro_ml_in_bioinformatics.ipynb](../1.1_intro_ml_in_bioinformatics.ipynb). We will examine how auto-zooming axes can create an optical illusion and how anchoring the axes to zero resolves it:
  ```python
  plt.xlim(left=0)
  plt.ylim(top=170)
  ```

---

## 2. Review of Takeaway Exercises
* **Problem Formulation Review:** Discussion and short presentations of our formulations for the four biological scenarios (Epigenetic Clock, Antimicrobial Resistance, Chemotherapy Sensitivity, and Viral Subtypes) from [problem_formulation_tool.ipynb](../problem_formulation_tool.ipynb).
* **Clinical Cohort Cleanup Review:** Reviewing [1.2_data_preprocessing_part_a.ipynb](../1.2_data_preprocessing_part_a.ipynb).

---

## 3. Theory (The 5-Stage Learning Ladder)
* **Topic: Numerical Data Transformations**
  * *Theory Primer:* [1.2_data_transformations_primer.md](../1.2_data_transformations_primer.md)
  * Why raw magnitudes (e.g., patient age vs. platelet count) mislead distance-based algorithms and gradient descent.
  * Distinguishing upstream biological normalization (CPM/TPM library depth adjustments) from downstream machine learning transformations.
  * The 4 core transformations:
    1. **Log Transformation ($\log_2(X + 1)$):** Compressing extreme right-skewed sequencing read distributions and variance stabilization.
    2. **Z-Score Standardization (`StandardScaler`):** Centering continuous variables to zero mean ($\mu = 0$) and unit standard deviation ($\sigma = 1$).
    3. **Min-Max Normalization (`MinMaxScaler`):** Rescaling values into bounded intervals ($[0.0, 1.0]$) for imaging and bounded physical sensor channels.
    4. **Robust Scaling (`RobustScaler`):** Using order statistics (median and IQR) to resist distortion from severe biological outliers (e.g., acute septic shock CRP spikes).
  * **Decision Framework:** Applying the transformation decision tree to select the right tool based on distribution shape and clinical constraints.

---

## 4. Hands-On Practical & Deliverables
* **Primary Computing Environment:** Visual Studio Code (`gcu-aiml-bioinfo` Conda kernel)
* **Interactive Notebook:** [1.2_data_preprocessing_part_b.ipynb](../1.2_data_preprocessing_part_b.ipynb)
* **Walkthrough Highlights:**
  * Visualizing feature scale dominance using clinical scatter plots.
  * Generating publication-grade diagnostic plots (marginal horizontal boxplots paired with distribution histograms) before and after transformations.
  * Evaluating `StandardScaler` collapse vs. `RobustScaler` resilience under severe outlier conditions.
* **📌 Takeaway Exercises & Deliverables for Day 5:**
  - [ ] Complete the *Student Challenge: Multi-Omics Patient Matrix Preparation* at the end of [1.2_data_preprocessing_part_b.ipynb](../1.2_data_preprocessing_part_b.ipynb).
