---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 3.2 / Applied Practicals — Lab Exercise 01
scheduled_dates: Week 8 (Day 16)
document_type: Session Agenda
ai_tier: "Tier 3: AI Collaboration (Disclosed)"
---

# Session 16: Lab Exercise 01 — End-to-End Binary Classification Pipeline

**Course Code:** `02BMSBI24365` — AI and ML in Bioinformatics  
**Primary Computing Environment:** Visual Studio Code (`gcu-aiml-bioinfo` Conda environment)  
**Interactive Notebook:** [lab_01_binary_classification_pipeline.ipynb](lab_01_binary_classification_pipeline.ipynb)  
**Cohort Dataset:** [data/tcga_brca_expression.csv](data/tcga_brca_expression.csv)  

---

## 📌 Session Roadmap

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      DAY 16 EXECUTION ROADMAP                          │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Clinical Grounding & cBioPortal Exploration                         │
│    • Real-world PAM50 cohort: Luminal A (ESR1+) vs. Basal (TNBC-like)  │
│ 2. Methodological Standards                                            │
│    • Zero-leakage rule: fit scaler strictly on training split          │
│    • Asymmetric cost: tune threshold to avoid False Negatives          │
│ 3. Hands-On Pipeline Execution (Stages 1–8)                            │
│    • Data ingestion, QC & 2D PCA transcriptomic projection             │
│    • Stratified split & ANOVA biomarker ranking                        │
│    • Triad modeling: Logistic Regression, Random Forest, Keras ANN     │
│ 4. Takeaways & Challenge Sprints                                       │
│    • Benchmarking (Stage 9) & 5-gene point-of-care panel (Stage 10)    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Clinical Grounding & cBioPortal Walkthrough

* **Cohort:** TCGA-BRCA primary tumor gene expression profiles ($n = 670, p = 60$).
* **Molecular Subtype Hallmarks:**
  * **Luminal A (`BRCA_LumA`):** Hormone-receptor positive (ER+/PR+); characterized by high *ESR1*, *PGR*, and *GATA3*; responsive to endocrine therapy.
  * **Basal-like (`BRCA_Basal`):** Hormone-receptor negative (TNBC-like phenotype); high expression of basal cytokeratins (*KRT5*, *KRT14*), *EGFR*, and mitotic drivers (*MKI67*); aggressive, requiring cytotoxic chemotherapy.
* **The Clinical Cost Matrix:**
  * Missing a Basal-like tumor as Luminal A (False Negative) deprives a high-risk patient of urgent chemotherapy.
  * We tune our classification decision thresholds ($\tau$) to maximize sensitivity and minimize False Negatives.

---

## 2. Core Methodological Standards

* **Strict Zero Data Leakage:** Preprocessing transformers (`StandardScaler`) must be fitted exclusively on `X_train` and applied to `X_test`. Never scale the full cohort prior to splitting.
* **Model Triad Suite:**
  1. **Logistic Regression:** Linear baseline providing interpretable log-odds and gene Odds Ratios ($\text{OR} = e^{w_j}$).
  2. **Random Forest:** Ensemble of 100 decision trees capturing non-linear epistatic interactions via Gini Importance.
  3. **Keras ANN:** Multi-layer perceptron with Dropout ($0.30, 0.20$) to prevent memorization in $p \gg n$ regimes.

---

## 3. Hands-On Pipeline Execution (Stages 1–8)

We work through [lab_01_binary_classification_pipeline.ipynb](lab_01_binary_classification_pipeline.ipynb) across three sequential checkpoints:

1. **QC & Dimensionality Reduction (Stages 1–3):** Ingest TCGA-BRCA raw expression, audit for zero missing values, plot hallmark distributions (*ESR1*, *GATA3*, *KRT5*, *MKI67*), and render 2D PCA projections.
2. **Partitioning & Feature Selection (Stages 4–5):** Perform stratified 80/20 train/test split, apply leak-free standard scaling, and rank top discriminative biomarkers using ANOVA F-tests.
3. **Sequential Model Training (Stages 6–8):**
   * *Block 1 (Logistic Regression):* Train linear baseline, compute confusion matrix, and extract gene odds ratios.
   * *Block 2 (Random Forest):* Train 100-tree ensemble, compute metrics, and inspect Gini feature importance.
   * *Block 3 (Keras ANN):* Train MLP with Dropout for 50 epochs, plot training vs. validation loss, and evaluate threshold shifts.

---

## 4. Takeaways & Next Steps

* **Stage 9 (Benchmark Synthesis):** Compile the side-by-side comparison table (Accuracy, Precision, Recall, F1, ROC-AUC) and combined ROC curves.
* **Stage 10 (Student Challenge):** Retrain the model triad using only the minimal 5-gene point-of-care signature (*FOXA1*, *CDC20*, *MELK*, *KIF2C*, *EXO1*) to evaluate diagnostic performance retention against the full 60-gene panel.
