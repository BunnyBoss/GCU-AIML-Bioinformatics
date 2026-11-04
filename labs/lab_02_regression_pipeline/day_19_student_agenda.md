---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 2.3 & 2.4 — Applied Practicals (Lab Exercise 02)
scheduled_dates: Week 10 (Day 19)
document_type: Session Agenda
ai_tier: "Tier 3: AI Collaboration (Disclosed)"
---

# Session 19: Lab Exercise 02 — End-to-End Regression Pipeline & Clinical Prediction

**Course Code:** `02BMSBI24365` — AI and ML in Bioinformatics  
**Primary Computing Environment:** Visual Studio Code (`gcu-aiml-bioinfo` Conda environment)  
**Primary Practical Guide:** [README.md](README.md)  
**Interactive Notebook:** [lab_02_regression_pipeline.ipynb](lab_02_regression_pipeline.ipynb)  
**Cohort Raw Dataset:** [../../datasets/raw/lab_02_day_19_diabetes_regression_raw.csv](../../datasets/raw/lab_02_day_19_diabetes_regression_raw.csv)  

---

## 📌 Session Roadmap

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      DAY 19 EXECUTION ROADMAP                          │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Recap & Unit Arc Transition                                         │
│    • From discrete classification boundaries to continuous regression  │
│    • Zero data leakage invariant: fit all transformers on train split  │
│ 2. Dual-Track Administrative Catch-Up                                  │
│    • Track A: Day 10 Comprehensive Make-Up Quiz (Closed-Book, Tier 1)  │
│    • Track B: Student group project analysis presentations             │
│ 3. Methodological Briefing: Continuous Error Geometry                  │
│    • Metrics: MAE (linear) vs. MSE/RMSE (quadratic) vs. R²             │
│    • Regularization (Ridge) vs. Ensembles (Random Forest, Boosting)    │
│ 4. Hands-On Practical: Lab 02 End-to-End Regression Pipeline           │
│    • Data hygiene: deduplication, anomaly removal, median imputation   │
│    • Model triad: Parameter tuning, training & observed result audit   │
│    • Benchmark synthesis table & linear vs. ensemble complexity trade-off│
│ 5. Takeaways & Deliverables                                            │
│    • Code hygiene (`nbstripout`) & GitHub Issue milestone submission   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Recap & Unit Arc Transition

* **Continuous vs. Categorical Phenotypes:** In Lab 01, we stratified breast cancer patients into discrete PAM50 subtypes (Luminal A vs. Basal). In clinical practice, many biological phenomena are continuous—such as viral load, quantitative gene expression, drug response ($IC_{50}$), and disease progression.
* **The Methodological Standard:**
  * In regression, error is continuous: $e_i = y_i - \hat{y}_i$.
  * All scalers (`StandardScaler`) must be fitted exclusively on the training split (`X_train`) to guarantee zero data leakage.

---

## 2. Dual-Track Session Split

### Track A: Day 10 Comprehensive Assessment Quiz (Quiet Exam Zone)
* **Target Cohort:** Students who were absent during Days 10–17.
* **Assessment Tier:** **Tier 1: No AI** (Closed-book, individual work).
* **Reference Resource:** [Day 10 Comprehensive Assessment Quiz](../../assessments/day_10_comprehensive_quiz/day_10_comprehensive_quiz.md).

### Track B: Student Group Milestone Presentations (Collaborative Studio)
* **Target Cohort:** Student project groups with pending analysis presentations.
* **Objective:** Present the exploratory data analysis, feature distributions, and preliminary baseline models from ongoing group projects.

---

## 3. Methodological Briefing: Continuous Error Geometry & Regression Metrics

* **Continuous Loss Metrics:**
  * **Mean Absolute Error (MAE):** $\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$. Penalizes errors linearly; resistant to extreme biological outliers.
  * **Root Mean Squared Error (RMSE):** $\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$. Penalizes large clinical errors quadratically.
  * **Coefficient of Determination ($R^2$):** $R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$. Quantifies the fraction of total outcome variance explained by the model relative to guessing the sample mean.

---

## 4. Hands-On Practical: Lab 02 Regression Pipeline

Work directly inside [lab_02_regression_pipeline.ipynb](lab_02_regression_pipeline.ipynb):

1. **Step 1 — Ingestion:** Ingest raw clinical features from `datasets/raw/lab_02_day_19_diabetes_regression_raw.csv`.
2. **Step 2 — Data Hygiene Pass:**
   * Audit and eliminate duplicate patient records via `df.drop_duplicates()`.
   * Screen and filter non-fitting clinical values (corrupted negative ages, impossible blood pressure/BMI readings).
   * Quantify missing values and impute using median strategies via `SimpleImputer`.
3. **Step 3 — Exploratory Data Analysis:** Examine target distribution skewness and plot the feature correlation heatmap.
4. **Step 4 — Leak-Free Partitioning:** Split data into $80\%$ Train and $20\%$ Test, fitting `StandardScaler` strictly on `X_train`.
5. **Step 5 — Model Triad Benchmarking (Parameter Rationale & Result Audit):**
   * *Model 1 (Ridge):* Understand $\alpha = 1.0$ regularization strength; inspect standardized weights ($w_j$).
   * *Model 2 (Random Forest):* Understand `n_estimators=100`, `max_depth=6`, and `min_samples_split=5`; inspect Gini importances.
   * *Model 3 (Gradient Boosting):* Understand shrinkage `learning_rate=0.05` and shallow tree depth `max_depth=3`.
6. **Step 6 — Benchmark Synthesis & Complexity Trade-Off:**
   * Compile the comparative benchmark synthesis table (Train $R^2$, Test $R^2$, MAE, RMSE).
   * Analyze why regularized linear models can outperform complex non-linear ensembles on small clinical cohorts.

---

## 5. Takeaways & Deliverables

* [ ] **Preserve Execution Outputs:** Save your executed notebook with all cell outputs (correlation heatmaps, coefficient plots, and benchmark tables) intact.
* [ ] **Group Submission via GitHub Issues:** One designated student from your group submits the lab milestone following the group submission protocol and template in [README.md](README.md#7-submission--evaluation-rubric).
* [ ] **Individual Portfolios:** All group members retain a copy of the executed notebook and data script in their own personal GitHub repository.
* [ ] **Institutional Schedule Reminder:** College is non-functional on Day 20 due to a faculty development training event; our next session reconvenes next week.
