# Laboratory Practicals: AI & ML in Bioinformatics

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  
**Practicals Overview:** 10 Structured Hands-on Computational Biology Experiments  

---

## Laboratory Structure & Guidelines

Every practical folder in this directory represents a hands-on computational biology experiment designed to bridge theoretical algorithms with real-world biological and clinical datasets.

Each lab adheres to a standardized pedagogical format:
1. **Biological Context & Problem Statement:** Why this computational task matters in genomics, oncology, or drug discovery.
2. **Dataset & Feature Dictionary:** Schema of biological inputs, units of measurement, and target ground truth.
3. **Algorithmic Implementation:** Step-by-step code walkthrough utilizing Python, Scikit-learn, TensorFlow/Keras, and specialized bioinformatics libraries.
4. **Diagnostic Metrics & Evaluation:** Rigorous statistical evaluation (ROC-AUC, Precision-Recall, Confusion Matrices, $R^2$, RMSE).
5. **Independent Student Challenge:** An unguided problem extension designed to test your ability to adapt the algorithm to a novel biological condition or dataset.

---

## Laboratory Practicals Index

| Lab # | Directory | Experiment Title | Primary Dataset & Biological Problem | Primary Packages |
|---|---|---|---|---|
| **01** | [lab_01_expression_preprocessing/](lab_01_expression_preprocessing/) | **RNA-seq Expression Preprocessing & Normalization** | Raw RNA-seq count matrix; library size normalization ($\log_2(\text{CPM}+1)$), quantile scaling, and KNN imputation. | `pandas`, `numpy`, `scipy` |
| **02** | [lab_02_biological_regression/](lab_02_biological_regression/) | **Epigenetic Clock: Biological Age Prediction** | DNA methylation beta values (Illumina Infinium arrays); Ridge & Lasso regression to estimate patient epigenetic age. | `scikit-learn`, `seaborn` |
| **03** | [lab_03_tumor_classification/](lab_03_tumor_classification/) | **Breast Cancer Biopsy Diagnosis** | Wisconsin Diagnostic Breast Cancer (WDBC) dataset; comparing Logistic Regression, Decision Trees, and Random Forests. | `scikit-learn`, `matplotlib` |
| **04** | [lab_04_evaluation_metrics_roc/](lab_04_evaluation_metrics_roc/) | **Clinical Diagnostic Metrics & ROC-AUC Analysis** | Skewed clinical cohort (rare disease biomarker panel); threshold tuning, Sensitivity/Specificity, PR curves, and ROC-AUC. | `scikit-learn`, `yellowbrick` |
| **05** | [lab_05_unsupervised_pca_clustering/](lab_05_unsupervised_pca_clustering/) | **Cancer Subtyping via PCA & $K$-Means** | High-dimensional tumor transcriptome ($20,000$ genes); PCA variance explained, t-SNE projection, and $K$-Means patient stratification. | `scikit-learn`, `scipy` |
| **06** | [lab_06_ann_keras_workflow/](lab_06_ann_keras_workflow/) | **Artificial Neural Networks with TensorFlow/Keras** | Multi-class tumor staging from blood serum proteomic profiles using a Multilayer Perceptron (ANN) with Dropout. | `tensorflow`, `keras` |
| **07** | [lab_07_histopathology_cnn/](lab_07_histopathology_cnn/) | **Histopathology Image Classification via 2D-CNN** | Hematoxylin and Eosin (H&E) stained tissue image patches; training a 2D Convolutional Neural Network for automated tumor detection. | `tensorflow`, `opencv-python` |
| **08** | [lab_08_sequence_classification_1dcnn_lstm/](lab_08_sequence_classification_1dcnn_lstm/) | **Genomic Sequence Motif Detection via 1D-CNN & LSTM** | One-hot encoded DNA promoter sequences; detecting Transcription Factor Binding Sites (TFBS) using 1D-CNN and LSTM. | `keras`, `biopython` |
| **09** | [lab_09_xai_shap_biomarkers/](lab_09_xai_shap_biomarkers/) | **Model Interpretability & Biomarkers using SHAP** | TreeSHAP and KernelSHAP on diagnostic cancer models; extracting top gene drivers and generating patient-level force plots. | `shap`, `scikit-learn` |
| **10** | [lab_10_capstone_project/](lab_10_capstone_project/) | **Capstone: End-to-End Multi-Omics Disease Pipeline** | Multi-omics patient survival analysis combining gene expression, clinical data, and somatic mutation status with full XAI audit. | Full ML/DL Stack |

---

## Lab Execution & Submission Protocol

1. **Working in Virtual Environments:**
   Always ensure your `gcu-aiml-bioinfo` Conda environment is active before starting:
   ```bash
   conda activate gcu-aiml-bioinfo
   ```
2. **Notebook Cleanliness (`nbstripout`):**
   Prior to submitting code or pushing to your repository fork, clean notebook execution outputs so large figures and raw tables do not inflate the Git history:
   ```bash
   pre-commit run --all-files
   ```
3. **Assessment & Grading:**
   Laboratory performance constitutes a major component of your Continuous Internal Assessment (CIA). Refer to [assessments/README.md](../assessments/README.md) for detailed evaluation rubrics and submission deadlines.
