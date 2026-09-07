# Unit 4: AI Applications in Bioinformatics

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  

---

## Unit Overview

The true power of artificial intelligence in biology is realized when models transition from benchmark datasets into real-world translational medicine, discovery biology, and clinical decision support.

Unit 4 is the integrative capstone unit of the theoretical curriculum. You will explore multi-omics data integration (combining genomics, transcriptomics, and clinical variables), functional sequence motif detection, and the critical field of **Explainable AI (XAI)**—using SHAP (SHapley Additive exPlanations) and LIME to transform black-box predictive models into biologically actionable insights.

---

## Core Topics & Syllabus Breakdown

### 4.1 Biological Data Analysis Using Machine Learning
* **Multi-Omics Data Fusion:** Strategies for combining disparate data modalities (genomic variants, RNA-seq expression, DNA methylation, and clinical survival metrics).
* **Early vs. Late Fusion:** Concatenating features before model training vs. ensemble blending of modality-specific sub-models.
* **Survival Analysis with ML:** Censored biological data, Kaplan-Meier curves, Cox Proportional Hazards, and Random Survival Forests for patient prognostic modeling.

### 4.2 Sequence Analysis Using Machine Learning
* **Motif Discovery & Identification:** Detecting regulatory binding sites (promoters, enhancers, splice sites) without alignment.
* **Protein Family Classification:** Encoding amino acid sequences and classifying proteins into homologous functional families and structural classes.
* **Variant Pathogenicity Prediction:** Predicting whether non-synonymous Single Nucleotide Variants (snps/missense mutations) are benign or disease-causing.

### 4.3 Model Interpretation & Evaluation: Explainable AI (XAI)
* **The "Black Box" Dilemma in Medicine:** Why high accuracy is insufficient for clinical adoption without biological interpretability and mechanistic plausibility.
* **SHAP (SHapley Additive exPlanations):**
  * Game-theoretic foundation (Shapley values from cooperative game theory).
  * Additive feature attribution: Fairly distributing the model output delta among input features.
  * **TreeSHAP:** Exact, polynomial-time Shapley values for tree ensembles (Random Forest, XGBoost).
  * **DeepSHAP:** Approximating feature importance in deep neural networks.
  * **Visual Interpretation:** Summary beeswarm plots, feature dependence plots, and local patient force plots.
* **LIME (Local Interpretable Model-agnostic Explanations):**
  * Approximating arbitrary non-linear models locally with an interpretable sparse linear surrogate.
* **Extracting Novel Biomarkers:** Moving from model explanation to biological discovery—validating top SHAP features against PubMed literature and Gene Ontology (GO) biological pathways.

---

## Associated Laboratory Practicals

* **[Lab 09](../../labs/lab_09_xai_shap_biomarkers/):** Model Interpretability & Biomarker Attribution using SHAP and LIME on Cancer Diagnostics.
* **[Lab 10](../../labs/lab_10_capstone_project/):** Capstone Project: End-to-End Multi-Omics Disease Prediction Pipeline with Full Explainability Audit.

---

## Key Questions Addressed in this Unit

1. *How do we validate that an AI model is learning genuine biological signal rather than technical batch effects?*
2. *How can an oncologist understand which specific gene mutations influenced an AI's treatment recommendation for an individual patient?*
3. *What are the ethical, regulatory, and validation guidelines governing the deployment of AI medical diagnostics in clinical practice?*
