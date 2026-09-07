# Unit 2: Machine Learning Techniques

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  

---

## Unit Overview

Unit 2 transitions from continuous estimation into discrete disease diagnosis, unsupervised patient stratification, and production-grade evaluation workflows.

High-throughput biological studies typically confront the **curse of dimensionality** ($p \gg n$), where thousands of biomarker measurements are available for only dozens or hundreds of patient cohorts. In this unit, you will master decision boundaries, tree-based ensemble methods, support vector classification, unsupervised dimensionality reduction (PCA, t-SNE), and cross-validation strategies designed to prevent data leakage in clinical AI.

---

## Core Topics & Syllabus Breakdown

### 2.1 Supervised Learning — Classification
* **Logistic Regression:** Sigmoid activation $\sigma(z) = \frac{1}{1 + e^{-z}}$, log-loss function, and odds ratios in clinical risk scoring.
* **Decision Trees & Information Theory:** Recursive binary splitting, Entropy, and Gini Impurity for biological rule extraction.
* **Ensemble Methods:**
  * **Random Forest:** Bagging (Bootstrap Aggregating) + random feature subspace selection for high-dimensional stability and feature importance rankings.
  * **Support Vector Machines (SVM):** Maximum margin hyperplanes, soft margins ($C$ parameter), and kernel tricks (RBF) for non-linear biological decision surfaces.

### 2.2 Unsupervised Learning — Clustering & Dimensionality Reduction
* **$K$-Means Clustering:** Centroid initialization, Voronoi tessellation, inertia, and determining optimal clusters via the Elbow method and Silhouette analysis.
* **Hierarchical Clustering:** Agglomerative clustering, linkage criteria (Ward, Complete, Average), and dendrogram generation for phylogenetic and expression profiling.
* **Principal Component Analysis (PCA):** Eigen-decomposition of covariance matrices, variance explained ratio, and compressing 20,000 genes into informative 2D/3D projections.
* **Non-linear Embeddings:** Intuition of t-Distributed Stochastic Neighbor Embedding (t-SNE) for single-cell clustering visualization.

### 2.3 Model Evaluation, Validation & Clinical Optimization
* **The Confusion Matrix:** True Positives (TP), False Positives (FP), True Negatives (TN), False Negatives (FN).
* **Clinical Diagnostic Trade-offs:**
  * Why Accuracy fails under heavy class imbalance (e.g., rare diseases affecting 0.1% of patients).
  * Sensitivity (Recall) vs. Specificity: Minimizing false negatives in clinical screening.
  * Precision, F1-Score, and the Matthews Correlation Coefficient (MCC).
* **Receiver Operating Characteristic (ROC):** ROC curves, False Positive Rate vs. True Positive Rate, and Area Under the Curve (ROC-AUC).
* **Precision-Recall Curves:** Superior metric for severely skewed biological cohorts.
* **Validation Hygiene:** $k$-Fold Cross-Validation, Stratified $k$-Fold, and avoiding data leakage between training and testing splits.

### 2.4 Machine Learning Pipelines
* **Scikit-learn Pipelines:** Encapsulating imputation, scaling, PCA, and classification into reproducible, single-execution pipelines to guarantee airtight cross-validation.

---

## Folder Contents & Key Materials

| File / Resource | Type | Description |
|---|---|---|
| [deep_dive_classification.md](deep_dive_classification.md) | Technical Guide | Complete mathematical and practical breakdown of Logistic Regression, Trees, Random Forests, and SVMs. |
| [deep_dive_unsupervised.md](deep_dive_unsupervised.md) | Technical Guide | In-depth theory on $K$-Means, Hierarchical clustering, distance metrics, and PCA mathematical formulation. |
| [assets/](assets/) | Visual Diagrams | Architecture diagrams, decision boundary plots, and confusion matrix visualizations. |

---

## Associated Laboratory Practicals

* **[Lab 03](../../labs/lab_03_tumor_classification/):** Breast Cancer Diagnosis: Comparing Logistic Regression, Decision Trees, and Random Forests.
* **[Lab 04](../../labs/lab_04_evaluation_metrics_roc/):** Diagnostic Metric Evaluation: Precision-Recall Curves, ROC-AUC, and Threshold Optimization.
* **[Lab 05](../../labs/lab_05_unsupervised_pca_clustering/):** Patient Subtyping: Dimensionality Reduction via PCA and Unsupervised Clustering of Gene Expression.

---

## Learning Objectives Checklist

By the end of this unit, you will be able to:
- [ ] Select appropriate classification algorithms based on dataset size and feature-to-sample ratio.
- [ ] Diagnose whether high training accuracy is genuine or a consequence of diagnostic class imbalance.
- [ ] Implement PCA from scratch or via Scikit-learn and project high-dimensional omics samples onto principal components.
- [ ] Formulate a leak-free Machine Learning Pipeline incorporating preprocessing, feature selection, and model tuning.
