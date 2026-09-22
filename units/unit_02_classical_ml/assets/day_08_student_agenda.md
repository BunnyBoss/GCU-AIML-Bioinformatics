---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 2 — Machine Learning Techniques
scheduled_dates: Week 4 / Lecture 2
document_type: Session Agenda
ai_tier: Full AI (Learning Aid)
---

# Session 08: Unsupervised Learning — PCA & Clustering

---

## 1. Recap

* **Grouping Unknown Fruits:** We will revisit the fruit sorting infographic from [deep_dive_unsupervised.md](../deep_dive_unsupervised.md): imagine being handed a basket of unknown, unlabeled exotic fruits. We naturally group them by observing physical **features** (color, weight, shape, texture).
* **The Core Definition of Unsupervised Learning:**
  * **Features Only (No Target Labels):** Unlike supervised learning, there is no teacher and no target column ($y$). We are given only the input measurements ($X$).
  * **Clustering:** Identifying natural groupings or hidden patterns among samples based purely on feature similarities.
  * **Natural vs. Machine Learning:** Humans group objects through visual intuition; machine learning algorithms group samples by calculating mathematical distances between feature values.

---

## 2. Review of Takeaway Exercises

* We will review the takeaway challenge from Day 07 ([2.3_model_evaluation_metrics.ipynb](../2.3_model_evaluation_metrics.ipynb)):
  * **Clinical Classification Tradeoffs:** Discussing student scenarios where **Sensitivity/Recall** must be prioritized (screening for fatal illnesses like PKU or pancreatic cancer) versus where **Precision** is paramount (avoiding invasive surgical resection or toxic procedures).
  * **The Accuracy Trap:** Why 99.9% accuracy is clinically useless on rare disease cohorts with 0.1% prevalence, and why we evaluate with the $F_1$-score.
  * **Pharmacokinetic Error Interpretation:** Comparing models where $\text{RMSE} \gg \text{MAE}$, identifying dangerous outlier spikes that could cause fatal patient overdoses.

---

## 3. Theory

*Complete conceptual primer available in [2.2 Unsupervised Learning Primer](../2.2_unsupervised_learning_primer.md).*

### Topic A: Dimensionality Reduction (PCA & t-SNE)
* **The High-Dimensional Challenge ($p \gg n$):** In high-throughput genomics, we often measure 20,000 genes for only 100 patients. We need dimensionality reduction to remove noise, eliminate redundant signals, and visualize complex datasets in 2D/3D.
* **When to Use:**
  * **PCA (Linear):** Fast and reliable; projects data along straight orthogonal axes to capture maximum global variance. Use for data exploration and as a preprocessing step before clustering or supervised modeling.
  * **t-SNE (Non-linear):** Focuses on preserving local neighbor relationships, mapping complex structures into distinct cell-type "islands". Exclusively for 2D/3D visual exploration (e.g., single-cell RNA-seq). *Rule:* Never use t-SNE coordinates as feature inputs for downstream machine learning models.

### Topic B: Unsupervised Clustering (K-Means & Hierarchical)
* **What & Why:** Grouping patient biopsies or molecular profiles without any predefined diagnostic labels.
* **K-Means (Partition-Based):**
  * Randomly initializes $K$ centroids, assigns samples to the closest centroid, and recalculates centroid centers iteratively until stable.
  * Selecting $K$: Using the **Inertia Elbow Method** (diminishing returns) and the **Silhouette Score** (cluster tightness vs. separation).
* **Hierarchical Clustering (Connectivity-Based):**
  * Bottom-up agglomeration: every sample starts as its own cluster and merges step-by-step into a **Dendrogram** tree.
  * Slicing the dendrogram horizontally reveals distinct biological subtypes.
* **Clustermaps:** Simultaneously clustering both patient samples (rows) and co-regulated gene modules (columns) to visualize functional biological pathways.

### Topic C: The Cooperative Bioinformatic Workflow
* **The Standardization Rule:** Always apply `StandardScaler` ($Z$-score normalization) first so high-magnitude features (like *GAPDH* expression) do not overpower low-magnitude regulatory genes (like *TP53*).
* **The 3-Step Pipeline:**
  $$\text{Raw Features } (X) \xrightarrow{\text{StandardScaler}} \text{Scaled Data} \xrightarrow{\text{PCA (Top PCs)}} \text{PCA Space} \xrightarrow{\text{K-Means}} \text{Discovered Subtypes}$$

---

## 4. Hands-On

**Primary Computing Environment:** Visual Studio Code (`gcu-aiml-bioinfo` Conda kernel).

* **Interactive Notebook:** [2.2_unsupervised_learning.ipynb](../2.2_unsupervised_learning.ipynb)
* **Hands-on Guided Walkthrough:**
  1. *Scale Disparity Demonstration:* Inspect raw morphometric scale differences (`mean area` vs. `mean fractal dimension`) and apply `StandardScaler`.
  2. *PCA Fitting & Scree Plot:* Fit PCA on all 30 features, verify variance explained by PC1 + PC2 (63.2%), and identify the elbow point.
  3. *Side-by-Side Comparison (PCA vs. t-SNE):* Visualize how linear PCA preserves global spread while non-linear t-SNE separates distinct patient islands.
  4. *K-Means Subtyping:* Fit K-Means ($K=2$) and visualize cluster separation directly in 2D PCA space.
  5. *Hierarchical Dendrogram:* Generate a Ward linkage dendrogram and apply a horizontal cut line ($y=55$).
  6. *Gene Co-Expression Clustermap:* Render a dual-dendrogram clustermap uncovering co-regulated gene expression modules.
  7. *Cooperative Pipeline:* Standardize $\to$ PCA (top 5 components) $\to$ K-Means clustering, verifying cleaner cluster separation with fewer dimensions.

---

## 📌 Deliverables for Next Session

* NA
