---
ai_tier: "Full AI (Learning Aid)"
---

# Sessions 05 & 06: Data Transformations Wrap-up, Model Evaluation Metrics & End-to-End ML Pipeline

**Course Code:** 02BMSBI24365 — AI and ML in Bioinformatics  
**Scheduled Dates:** Week 3 / Lectures 1 & 2  

---

## 1. Recap

**Git Courseware Synchronization ("Every Session Workflow"):**
* **Start of Session:** Run `./supplementary_resources/start_session.sh` to pull upstream updates and verify our isolated `student_space/` workspace.
* **Working Area:** We will copy notebooks into `student_space/` to guarantee personal edits are never overwritten or blocked by merge conflicts.
* **End of Session:** Run `./supplementary_resources/end_session.sh` to automatically stage and commit our day's work into local Git history.

**Immediate & Arc Recap:**
* We will revisit $\log_2(\text{CPM} + 1)$ variance stabilization for skewed biological count data.
* We will reconnect to the universal 4-step ML arc:
  $$\text{Dataset Preparation} \longrightarrow \text{Model Selection} \longrightarrow \text{Training} \longrightarrow \text{Evaluation}$$

---

## 2. Review of Takeaway Exercises

* **Review Task:** The analog classmate age collection exercise.
* **Companion Review Notebook:** [1.2_classmate_age_distribution_review.ipynb](../1.2_classmate_age_distribution_review.ipynb)

**Distribution Shape Analysis:**
* We will inspect the plotted cohort age curve ($N=28$) across the classroom.
* We will contrast parametric measures ($\mu$ mean, $\sigma$ standard deviation) with non-parametric measures ($\text{median}$, $\text{IQR}$).

**Bridge to Scaling:**
* We will connect distribution shape directly to scaler selection: why older scholars inflate the mean and compress `MinMaxScaler`, while `RobustScaler` (median, IQR) centers without distortion.
* Reference primer: [1.2 Data Transformations Primer](../1.2_data_transformations_primer.md).

---

## 3. Theory

### Data Transformations Wrap-up
* **StandardScaler:** Centering features to zero-mean and unit-variance ($z = \frac{x-\mu}{\sigma}$). Best for normal distributions and gradient-based models.
* **MinMaxScaler:** Compressing features into a fixed $[0.0, 1.0]$ bounding box. Best for distance-based algorithms ($k$-NN) and image data.
* **RobustScaler:** Scaling via median and Interquartile Range ($\frac{x - Q_2}{Q_3 - Q_1}$). Best for high-throughput biological data with heavy outlier spikes.

### Model Evaluation Metrics
*Complete conceptual primer available in [2.3 Model Evaluation Primer](../../unit_02_classical_ml/2.3_model_evaluation_primer.md).*

#### The Exam Analogy & The Cost of Being Wrong in Biology
Scoring $90\%$ on an exam sounds great—unless the $10\%$ missed were the safety protocols for a BSL-3 laboratory. In computational biology, we must carefully consider the cost of being wrong:
* **False Negative:** Malignant tumor missed $\longrightarrow$ patient denied early intervention, resulting in metastasis.
* **False Positive:** Healthy individual flagged $\longrightarrow$ unnecessary biopsies, toxic regimens, severe distress.
* **Regression Error:** Drug dose predicted incorrectly by $5\,\mu\text{M} \longrightarrow$ toxicity or ineffectiveness.

Performance grading must match the problem type: **Classification** vs. **Regression**.

#### Classification Metrics (Discrete Categories)
* **Confusion Matrix:** True Positive ($TP$), False Positive ($FP$), False Negative ($FN$), True Negative ($TN$).
* **Accuracy:** Overall proportion correct ($\frac{TP+TN}{\text{Total}}$); misleading in imbalanced biological cohorts.
* **Recall / Sensitivity:** $\frac{TP}{TP + FN}$ — fraction of sick patients detected (critical in cancer screening).
* **Precision:** $\frac{TP}{TP + FP}$ — confidence when an alarm is sounded (critical for invasive follow-ups).
* **Specificity:** $\frac{TN}{TN + FP}$ — fraction of healthy patients correctly cleared.
* **$F_1$-Score:** Harmonic mean of Precision and Recall ($2 \times \frac{P \times R}{P + R}$).
* **Discrimination Thresholds & ROC-AUC:** Trading off Sensitivity vs. Specificity across decision thresholds $\tau \in [0, 1]$.

#### Regression Metrics (Continuous Quantities)
* **Mean Absolute Error (MAE):** Average error magnitude in original physical units (linear penalty).
* **Mean Squared Error (MSE):** Squared error magnitude; heavily penalizes large clinical misses.
* **Root Mean Squared Error (RMSE):** Outlier-sensitive error converted back to original physical units ($\sqrt{\text{MSE}}$).
* **$R^2$ Score (Coefficient of Determination):** Proportion of phenotypic variance explained by the model ($1.0 = \text{perfect}$, $0.0 = \text{cohort mean}$).

### The End-to-End Leak-Free Pipeline
* **Zero Data Leakage Invariant:** Computing preprocessing parameters exclusively on training splits via `.fit()`, applying `.transform()` to test splits.
* **Scikit-learn Pipeline Architecture:** Atomic chaining of transformers and estimators to guarantee leak-free cross-validation.

---

## 4. Hands-On

**Primary Computing Environment:** Visual Studio Code (`gcu-aiml-bioinfo` Conda kernel).

### Part A: Complete Scaling in Existing Notebook
* Open [1.2_data_preprocessing_part_b.ipynb](../1.2_data_preprocessing_part_b.ipynb).
* Complete scaling comparisons (`StandardScaler`, `MinMaxScaler`, `RobustScaler`) and visualize before/after distributions.

### Part B: Diagnostic Metric Walkthrough
* Interactive notebook: [2.3_model_evaluation_metrics.ipynb](../../unit_02_classical_ml/2.3_model_evaluation_metrics.ipynb).
* Calculate confusion matrices, classification reports, ROC curves, and regression residuals.

### Part C: Master End-to-End ML Pipeline Notebook
* **Notebook File:** [2.4_end_to_end_ml_pipeline.ipynb](../../unit_02_classical_ml/2.4_end_to_end_ml_pipeline.ipynb)
* **Design Pattern:** We will construct the universal 4-step workflow structured into collapsable sections, tracking parallel biological tracks at every step:
  * **Track A (Classification):** Breast Cancer Wisconsin dataset (`load_breast_cancer`) $\to$ Malignant vs. Benign diagnosis.
  * **Track B (Regression):** Diabetes dataset (`load_diabetes`) $\to$ Quantitative disease progression score.
