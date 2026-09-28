---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 2 — Classical Machine Learning Algorithms
scheduled_dates: Week 5 / Lectures 1 & 2
document_type: Session Agenda
ai_tier: Full AI (Learning Aid)
---

# Sessions 09 & 10: Core Supervised Models (Regression & Classification)

---

```text
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                             DAY 09 & 10 INTEGRATED ROADMAP                                │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Recap & Admin Check-in (10 min)                                                        │
│    • Supervised Learning foundations (features X → ground-truth targets y)                │
│    • Continuous targets (Regression) vs. Categorical targets (Classification)             │
│    • Admin: Submitting takeaway exercises via GitHub Issues directly via browser          │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Review of Takeaway Exercises                                                           │
│    • NA (No formal takeaway exercises assigned)                                           │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Theory: Core Supervised Models                                                         │
│    • Regression Models ([2.1_regression_models_primer.md](../2.1_regression_models_primer.md))│
│         - Linear Regression (Best-fit line, residuals, biomarker weights, standardization)│
│         - Polynomial Regression (Dose-response saturation, feature expansion, overfitting)│
│         - Regression Evaluation Metrics (MAE, MSE, RMSE, R²)                              │
│    • Classification Models ([2.1_classification_models_primer.md](../2.1_classification_models_primer.md))│
│         - Logistic Regression (Binary labels, Sigmoid curve, Odds Ratios, thresholds)      │
│         - Decision Trees (Clinical flowcharts, Gini Impurity, IF/THEN rules, overfitting)  │
│         - Random Forests (Ensemble committee, Bagging, √p subspacing, feature importance) │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. Hands-On Practical & Deliverables                                                      │
│    • [2.1_regression_models.ipynb](../2.1_regression_models.ipynb) (Parts 1–5)             │
│    • [2.1_classification_models.ipynb](../2.1_classification_models.ipynb) (Parts 1–6)     │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Recap & Admin Check-in

* **Pre-Session Administrative Notice (GitHub Issues Submission):**
  * We submit takeaway exercises and code artifacts directly through the course GitHub repository in the browser:
    1. Navigate to the course GitHub repository in your browser.
    2. Click the **Issues** tab $\longrightarrow$ click **New Issue**.
    3. Title the issue: `[Takeaway] <Student Name> - <Topic>` and post your code snippet, test evaluation metrics, and a 2-sentence biological interpretation.
  * Browser-based issue submission avoids command-line Git roadblocks while establishing an auditable record of your laboratory milestones.
* **Supervised Learning Foundations:**
  * In supervised learning, models learn mathematical mappings from input features ($\mathbf{X}$) to known ground-truth target labels ($y$).
  * The two core supervised problem types:
    * **Regression:** The target $y$ is a continuous numerical measurement (e.g., survival time in months, drug $IC_{50}$ concentration, epigenetic biological age).
    * **Classification:** The target $y$ is a discrete category or clinical state (e.g., Benign vs. Malignant, Treatment Responder vs. Relapse).

---

## 2. Review of Takeaway Exercises

* **Review Task:** NA (No formal takeaway exercises were assigned in Session 08).

---

## 3. Theory: Core Supervised Models

### Topic A: Regression Models — Predicting Continuous Biological Measurements
*Assigned Primer: [2.1 Regression Models Primer](../2.1_regression_models_primer.md)*

* **The Clinical Question:** Predicting continuous clinical outcomes from molecular and cellular measurements (e.g., progression-free survival in months, drug $IC_{50}$ concentration, epigenetic biological age, antibody binding affinity $K_d$).
* **Linear Regression (Straight-Line Trends):**
  * *Equation:* $y = w_1 x_1 + w_2 x_2 + \dots + w_p x_p + b = \mathbf{w}^T \mathbf{x} + b$.
  * *Residuals & OLS:* The model finds the best-fit line by minimizing the sum of squared differences between true and predicted outcomes:
    $$\text{Residual}_i = y_i^{\text{actual}} - y_i^{\text{predicted}}, \quad \text{Minimize: } \sum_{i=1}^n (y_i - \hat{y}_i)^2$$
  * *Biological Meaning of Weights:* Each weight $w_j$ represents the change in outcome per 1-unit increase in Feature $j$, holding all other features constant. Positive weights indicate protective factors; negative weights indicate risk factors.
  * *Feature Standardization:* Encapsulating `StandardScaler` inside a `Pipeline` ensures fair coefficient comparison and prevents data leakage across features with vastly different physical scales.
* **Polynomial Regression (Curved Biological Trends & Saturation Kinetics):**
  * *Biological Saturation:* Biological systems frequently exhibit non-linear saturation (e.g., pharmacological dose-response curves, enzyme kinetics), where straight lines fail at plateaus.
  * *Feature Expansion Trick:* Synthesize higher-order terms from existing features ($x \to [x, x^2, x^3]$) and fit a linear model on the expanded table:
    $$\hat{y} = w_1 x + w_2 x^2 + w_3 x^3 + b$$
  * *Capacity Spectrum & Overfitting:*
    * *Degree 1 (Linear):* Underfits biological saturation.
    * *Degree 3 (Cubic):* Naturally captures biological inflection points and plateaus.
    * *Degree 10 (High-order):* Overfits experimental noise, generating non-biological oscillations.

---

### Topic B: Classification Models — Predicting Discrete Biological Categories & States
*Assigned Primer: [2.1 Classification Models Primer](../2.1_classification_models_primer.md)*

* **The Clinical Question:** Binary and categorical diagnostic determinations (e.g., Benign $0$ vs. Malignant $1$ on biopsy cytology, Chemotherapy Responder $1$ vs. Relapse $0$).
* **Logistic Regression (Biological Probabilities & S-Curves):**
  * *Where Linear Regression Breaks:* Straight lines extend to $\pm \infty$. On extreme biomarker inputs, linear models predict impossible probabilities (e.g., $-45\%$ or $+174\%$).
  * *The Sigmoid Function:* Compresses unbounded linear scores $z = \mathbf{w}^T\mathbf{x} + b$ into valid biological probabilities $P \in [0.0, 1.0]$:
    $$P(\text{Malignant} \mid \mathbf{x}) = \sigma(z) = \frac{1}{1 + e^{-z}} = \frac{1}{1 + e^{-(\mathbf{w}^T\mathbf{x} + b)}}$$
  * *Clinical Odds Ratios:* Exponentiating standardized weights yields Odds Ratios ($\text{OR} = e^{w_j}$):
    * $\text{OR} > 1.0$: Feature is a **Risk Factor** (multiplies disease odds).
    * $\text{OR} < 1.0$: Feature is **Protective / Normal** (reduces disease odds).
    * $\text{OR} = 1.0$: Feature has no diagnostic association.
  * *Decision Threshold ($\tau$) Tuning:* Default $\tau = 0.5$. In clinical oncology, missing cancer (**False Negative**) is potentially fatal, whereas a false alarm (**False Positive**) causes a manageable confirmatory biopsy. Lowering $\tau$ (e.g., to $0.15$) maximizes **Sensitivity / Recall**.
* **Decision Trees (Hard Clinical Rules & Flowcharts):**
  * *Discrete Clinical Rules:* Pathology guidelines operate on hard thresholds (IF/THEN).
  * *Gini Impurity:* Splits are chosen to maximize the reduction in Gini Impurity ($G = 1 - \sum_{k=1}^C p_k^2$).
  * *Root Node:* Represents the single most discriminative diagnostic threshold across the entire cohort (e.g., `worst perimeter <= 112.8 μm`).
  * *Model Auditability:* Tree logic can be inspected as plain-text clinical rules (`export_text`) or plotted as visual flowcharts (`plot_tree`).
  * *Overfitting Control:* Restricting depth (`max_depth=3`) yields robust, clinically generalizable rules.
* **Random Forests (The Committee of Experts):**
  * *Multidisciplinary Tumor Board Analogy:* Overcoming single-tree variance through an ensemble of $100+$ diverse trees.
  * *Two Layers of Diversity:*
    1. *Bootstrap Aggregating (Bagging):* Each tree trains on a random bootstrap sample drawn with replacement ($\approx 63.2\%$ unique patients).
    2. *Random Feature Subspaces:* At every split, only a random subset of features ($\sqrt{p}$) is evaluated, preventing dominant markers from masking secondary signals.
  * *Majority Consensus Voting:* Final classifications are established by majority vote, reducing prediction variance.
  * *Biomarker Discovery:* Ranking candidate biomarkers by **Mean Decrease in Impurity** (Gini Feature Importance).
* **Multi-Model Evaluation & Diagnostics:**
  * Head-to-head comparison of Logistic Regression, Decision Trees, and Random Forests.
  * Metrics: Accuracy, Sensitivity (Recall), Precision, F1-Score, ROC-AUC.
  * Diagnostic Visualizations: Multi-model ROC curves and Confusion Matrices.

---

## 4. Hands-On Practical & Deliverables

**Primary Computing Environment:** Visual Studio Code (`gcu-aiml-bioinfo` Conda kernel).

### Practical Track 1: Regression Modeling
* **Interactive Notebook:** [2.1_regression_models.ipynb](../2.1_regression_models.ipynb)
* **Guided Sequence (Streamlined Alignment with Theory Primer):**
  1. *Simple 1D Linear Regression:* Create dataset (Oncogene Expression vs. Survival Months with `np.random`), fit `LinearRegression`, extract slope $w$ and intercept $b$, and display scatter plot with best-fit line and model equation.
  2. *Multiple Linear Regression (Multi-Gene Model):* Add 2 more genes (`TP53`, `BRCA1`, `MYC`), fit `LinearRegression`, extract learned weights, and display the biomarker weights bar plot (protective vs. risk factor) alongside actual vs. predicted survival.
  3. *Polynomial Regression:* Create curved pharmacological dose-response dataset (drug concentration vs. cancer cell viability); apply polynomial feature expansion ($x \to [x, x^2, x^3]$) and fit linear regression; display plot contrasting straight-line underfitting against polynomial saturation curve, and print the learned equation.

### Practical Track 2: Classification Modeling
* **Interactive Notebook:** [2.1_classification_models.ipynb](../2.1_classification_models.ipynb)
* **Guided Sequence (Streamlined Alignment with Theory Primer):**
  1. *Logistic Regression:*
     * Demonstrate linear boundary failure vs. calibrated Sigmoid S-curve on the 8-patient pilot FNA cohort.
     * Fit multi-biomarker model on 60 biopsies, compute and plot clinical Odds Ratios ($\text{OR} = e^w$) to distinguish risk factors ($\text{OR} > 1.0$) from protective factors ($\text{OR} < 1.0$).
  2. *Decision Trees:*
     * Train depth-constrained clinical decision tree (`max_depth=2`) on cellular biomarkers.
     * Extract human-readable IF/THEN SOP rules using `export_text()`.
     * Render the visual diagnostic flowchart with node impurities and class balances via `plot_tree()`.
  3. *Random Forests:*
     * Train 100-tree ensemble mimicking a Multidisciplinary Tumor Board committee.
     * Extract and plot Gini Feature Importance (Mean Decrease in Impurity) to rank candidate biomarkers.

---

## 📌 Deliverables for Next Session

* [ ] **Challenge Deliverable (Submit via GitHub Issues):**
  Complete the takeaway exercise from either [2.1_regression_models.ipynb](../2.1_regression_models.ipynb) (Linear & Polynomial Regression modeling) or [2.1_classification_models.ipynb](../2.1_classification_models.ipynb) (Classification Models in Clinical Diagnostics).
  
  **How to Submit:**
  1. Open the course GitHub repository in your browser.
  2. Click the **Issues** tab $\longrightarrow$ click **New Issue**.
  3. Title your issue: `[Takeaway] <Student Name> - <Topic>`
  4. Post your completed Python code snippet, model output (equation, Odds Ratios, extracted rules, or feature importance), and a 2-sentence clinical/biological interpretation directly into the issue description.
