# Laboratory Practicals: AI & ML in Bioinformatics

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  
**Practicals Framework:** Hands-on Computational Biology Experiments  

---

## 1. Laboratory Structure & Pedagogical Standards

Every practical experiment in this laboratory curriculum bridges theoretical machine learning algorithms with real-world biological, genomic, and clinical datasets.

Each practical exercise follows a rigorous, reproducible 5-stage architecture:
1. **Biological Problem Statement:** Clinical context, molecular hallmarks, and the real-world significance of the computational phenotype.
2. **Dataset & Feature Dictionary:** Schema of biological inputs, gene expression/methylation levels, units of measurement, and clinical ground truth.
3. **Leak-Free Implementation:** Strict isolation between training and test sets using Scikit-Learn pipelines and deep learning workflows (no global scaling).
4. **Diagnostic Metrics & Clinical Calibration:** Rigorous evaluation metrics (Sensitivity/Recall, Specificity, ROC-AUC, PR Curves) and decision threshold tuning ($\tau$) tailored to asymmetric clinical costs.
5. **Independent Student Challenge:** An unguided problem extension designed to test your ability to adapt algorithms to novel biomarkers, loss penalties, or clinical cohorts.

---

## 2. Active Practical (Available Now)

| Practical | Directory | Title & Focus | Biological Cohort | Primary Stack | Status |
|---|---|---|---|---|---|
| **Lab Exercise 01** | [lab_01_binary_classification_pipeline/](lab_01_binary_classification_pipeline/) | **End-to-End Binary Classification Pipeline** | TCGA-BRCA RNA-seq Primary Tumors ($n = 670, p = 60$); PAM50 subtype prediction (Luminal A vs. Basal-like). | `pandas`, `scikit-learn`, `tensorflow` | 🟢 **Active** |

### Lab Exercise 01 Overview
* **Folder:** [labs/lab_01_binary_classification_pipeline/](lab_01_binary_classification_pipeline/)
* **Primary Deliverable:** [lab_01_binary_classification_pipeline.ipynb](lab_01_binary_classification_pipeline/lab_01_binary_classification_pipeline.ipynb)
* **Practical Guide:** [labs/lab_01_binary_classification_pipeline/README.md](lab_01_binary_classification_pipeline/README.md)
* **Dataset Asset:** `data/tcga_brca_expression.csv` (pre-assembled from raw TCGA cBioPortal files)
* **Key Tasks:**
  1. Ingest curated primary breast tumor cohort (670 patients $\times$ 60 PAM50 and oncogenic driver genes).
  2. Implement strict leak-free train/test partition ($80/20$) with training-only `StandardScaler`.
  3. Benchmark three complementary model families:
     * **Logistic Regression:** Linear baseline with gene Odds Ratios ($\text{OR} = e^{w_j}$).
     * **Random Forest:** 100-tree ensemble with Gini feature importance ranking.
     * **Keras ANN:** Deep multilayer perceptron with Dropout regularization and threshold calibration ($\tau$).
  4. Formulate a minimal 5-gene point-of-care diagnostic panel (*FOXA1*, *CDC20*, *MELK*, *KIF2C*, *EXO1*).

---

## 3. Semester Practical Curriculum Roadmap

The subsequent hands-on experiments will be released sequentially as the course progresses through deep learning architectures, sequence modeling, and explainable AI:

| Lab # | Experiment Focus | Biological Domain & Benchmark Problem | Target Stack | Curriculum Schedule |
|---|---|---|---|---|
| **01** | **Binary Classification Pipeline** | TCGA-BRCA PAM50 Subtype Classification (Luminal A vs. Basal) | `scikit-learn`, `tensorflow` | **Active (Day 16)** |
| **02** | **Biological Regression & Epigenetic Clocks** | DNA Methylation Beta Values; Age Prediction via Ridge/Lasso | `scikit-learn`, `scipy` | Scheduled |
| **03** | **Tumor Diagnosis & Decision Trees** | Diagnostic Fine-Needle Aspirate Features (WDBC); Ensemble Trees | `scikit-learn`, `seaborn` | Scheduled |
| **04** | **Clinical Metrics & Imbalanced Learning** | Rare Disease Cohort; PR-AUC, Threshold Tuning, Cost Matrices | `scikit-learn`, `yellowbrick` | Scheduled |
| **05** | **Unsupervised Clustering & PCA** | High-Dimensional Transcriptomic Profiling; PCA & $K$-Means | `scikit-learn`, `matplotlib` | Scheduled |
| **06** | **Deep Neural Networks (ANN)** | Proteomic Serum Profiles; Multi-layer Perceptron with Keras | `tensorflow`, `keras` | Scheduled |
| **07** | **Histopathology Image Classification** | Whole-Slide H&E Tissue Patches; 2D Convolutional Neural Networks | `tensorflow`, `opencv-python` | Scheduled |
| **08** | **Genomic Sequence Modeling** | DNA Promoter Motifs & TFBS Detection via 1D-CNN & LSTM | `tensorflow`, `biopython` | Scheduled |
| **09** | **Explainable AI (XAI) & Biomarker Extraction** | TreeSHAP and KernelSHAP Feature Attributions for Clinical Models | `shap`, `scikit-learn` | Scheduled |
| **10** | **Capstone Project** | End-to-End Multi-Omics Disease Prediction & Model Audit | Full ML/DL Stack | Scheduled |

---

## 4. Execution & Submission Guidelines

### Computational Environment
Always activate the course Conda environment before launching Jupyter:
```bash
conda activate gcu-aiml-bioinfo
```

### Git & Notebook Hygiene
Prior to committing work or submitting pull requests, clear large execution plots and binary outputs using `nbstripout`:
```bash
pre-commit run --all-files
```

### Submission Protocol via GitHub Issues
1. Complete the practical notebook, diagnostic plots, and the independent challenge extension.
2. Open a **New Issue** on the course repository titled:
   `[Lab Exercise 01 Submission] - <Your Name / Group Name>`
3. Embed your model comparison table, ROC-AUC curve visualization, 3-sentence biological takeaway, and AI tool disclosure statement following the rubric in [labs/lab_01_binary_classification_pipeline/README.md](lab_01_binary_classification_pipeline/README.md).
