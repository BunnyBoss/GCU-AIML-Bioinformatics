---

Biological Problem Decision Framework
* **Objective:** To learn how to structure any biological research question into a clear machine learning formulation.
* **Framework Tool:** [Student_Biological_Problem_Questionnaire.ipynb](./Student_Biological_Problem_Questionnaire.ipynb)

### In-Class Live Walkthrough Example: Tumor Classification
* **Biological Question:** Is a breast tissue biopsy sample benign or malignant?
* **Data Source:** TCGA Breast Invasive Carcinoma (BRCA) Dataset.
* **Features ($X$):** Clump thickness, uniformity of cell size, marginal adhesion, single epithelial cell size ($30$ numerical features).
* **Target ($y$):** Tumor diagnosis (`0 = Benign`, `1 = Malignant`).
* **Target Type:** Categorical (Discrete class).
* **ML Task Deduced:** **Supervised Learning $\longrightarrow$ Binary Classification**.

---

### In-Class & Takeaway Practice Scenarios

Open [Student_Biological_Problem_Questionnaire.ipynb](./Student_Biological_Problem_Questionnaire.ipynb) and complete the 5 steps for each of the following scenarios:

#### 🧪 Scenario A: Epigenetic Aging Clock
* **Context:** A longevity lab measures DNA methylation levels across $500$ CpG sites from blood samples to estimate a patient's true biological age in years.
* **Your Task:** Identify $X$, $y$, data dimensions, target type (Continuous vs. Categorical), and deduce the ML task (Regression).

#### 🧪 Scenario B: Antimicrobial Resistance (AMR) Detection
* **Context:** A microbiology institute sequences whole genomes of *Mycobacterium tuberculosis* isolates to determine whether each isolate is resistant or susceptible to Rifampicin.
* **Your Task:** Identify $X$ (SNP variants/mutations), $y$ (Resistant vs. Susceptible), target type, and deduce the ML task (Binary Classification).

#### 🧪 Scenario C: Chemotherapy Drug Sensitivity ($IC_{50}$ Prediction)
* **Context:** High-throughput screening measures RNA-seq expression of $1,000$ genes across cancer cell lines to predict the exact half-maximal inhibitory drug concentration ($IC_{50}$ in $\mu\text{M}$).
* **Your Task:** Identify $X$, $y$, target type, and deduce the ML task (Regression).

#### 🧪 Scenario D: Viral Subtype Discovery (Unsupervised Pattern Finding)
* **Context:** Researchers sequence 200 unknown viral genomes during an outbreak without any prior disease classification to see if they naturally group into distinct viral families.
* **Your Task:** Identify why this problem lacks a target variable $y$ and deduce the unsupervised task (Clustering / PCA).

---