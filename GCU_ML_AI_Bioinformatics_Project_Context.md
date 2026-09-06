# Master Project Context: ML & AI for Bioinformatics — GCU

## 1. Project Overview & Scope
This repository is the central workspace and master context router for the **"Machine Learning and AI for Bioinformatics"** curriculum (**Course Code: 02BMSBI24365**).

* **Institution:** Gordon City University (GCU), School of Sciences, Dept. of Life Sciences
* **Audience:** M.Sc. Bioinformatics (Semester III / Year 2)
* **Format:** 12-Week Master Curriculum + Hands-on Computer Labs
* **Scope:** Spans classical Machine Learning (Supervised regression/classification, Unsupervised clustering, Dimensionality reduction), advanced Deep Learning architectures (**ANNs, CNNs, RNNs/LSTMs, Transformers, Generative AI, and Agentic AI** in biology), and Explainable AI (SHAP, LIME).

---

## 2. Core Educational Objectives
1. **Classical & Deep Learning Mastery:** Transition from classical algorithms (Random Forest, SVM, $K$-Means, PCA) to deep neural architectures (ANNs, CNNs for biological imaging, RNNs/LSTMs for sequence analysis, and Transformers/LLMs for protein/genomic modeling).
2. **Biological Data Engineering:** Preprocessing, normalization, and biological sequence encoding ($k$-mers, one-hot matrices, embeddings).
3. **Biomarker & Target Discovery:** Feature selection and extraction for disease prognosis, survival analysis, and drug-target interaction.
4. **Explainable AI (XAI) & Clinical Trust:** Interpreting black-box models using SHAP/LIME for validated biological discovery.

---

## 3. Curriculum Structure & Module Index
> 📖 **Full syllabus text:** [assets/curriculum.txt](assets/curriculum.txt)  
> 🧬 **Detailed unit breakdown with biological analogies:** [Day1/course_unit_details.md](Day1/course_unit_details.md)

```
02BMSBI24365: AI AND ML IN BIOINFORMATICS
│
├── Unit 1: Foundations of Machine Learning for Bioinformatics
│   ├── 1.1 Introduction to ML in Bioinformatics (Supervised vs. Unsupervised)
│   ├── 1.2 Data Preprocessing & Feature Engineering (Imputation, Scaling, k-mers, One-Hot)
│   ├── 1.3 Supervised Learning – Regression (Linear, Polynomial, MSE, MAE, R²)
│   └── 1.4 Biological Data Regression Applications (Gene Expression, Epigenetic Age)
│
├── Unit 2: Machine Learning Techniques
│   ├── 2.1 Supervised Learning – Classification (Logistic Regression, Trees, Random Forest)
│   ├── 2.2 Unsupervised Learning – Clustering & PCA (K-Means, Hierarchical, PCA)
│   ├── 2.3 Model Evaluation & Optimization (Confusion Matrix, Precision/Recall, ROC-AUC, CV)
│   └── 2.4 ML Pipelines (End-to-end Scikit-learn Workflows)
│
├── Unit 3: Deep Learning for Biological Data
│   ├── 3.1 Artificial Neural Networks (ANNs & Backpropagation)
│   ├── 3.2 Deep Learning Frameworks (TensorFlow & Keras Implementation)
│   ├── 3.3 CNN & Sequence Models (CNNs for Bio-images, RNN/LSTM for Sequences)
│   └── 3.4 Transformers, Generative AI & Agentic AI (Attention, Protein LLMs, AlphaFold)
│
└── Unit 4: AI Applications in Bioinformatics
    ├── 4.1 Biological Data Analysis using ML (Multi-omics Disease Prediction)
    ├── 4.2 Sequence Analysis using ML (Motif Detection, Protein Family Classification)
    └── 4.3 Model Interpretation & Evaluation (Explainable AI: SHAP & LIME)
```

---

## 4. Hands-on Lab Experiments Index
> 🔬 **Reference:** See Section 5 of [assets/curriculum.txt](assets/curriculum.txt) for experiment guidelines.

* **Lab 1:** Preprocess gene expression dataset (Normalization & Imputation)
* **Lab 2:** Build regression model for biological measurements
* **Lab 3:** Train classification model (Random Forest for diagnosis)
* **Lab 4:** Evaluate model performance using Confusion Matrix & ROC-AUC
* **Lab 5:** Unsupervised clustering ($K$-Means on gene expression)
* **Lab 6:** Build Artificial Neural Network (ANN) using TensorFlow/Keras
* **Lab 7:** Apply CNN on biological/histopathology image dataset
* **Lab 8:** Biological sequence classification using 1D-CNN / LSTM
* **Lab 9:** Model interpretability & biomarker attribution using SHAP / LIME
* **Lab 10:** Capstone Mini-Project (Disease prediction or variant classification)

---

## 5. Core Teaching Philosophy & Pedagogical Rules
* **Pedagogical Progression:** Intuition $\to$ Biological Framing $\to$ Terminology $\to$ Minimal Math $\to$ Code Implementation.
* **Direct Student-Facing Address (Strict Rule):**
  * All generated learning material is student-facing.
  * **Write directly to the learner.** Never refer to learners as "students" in the content (e.g., avoid "teach students", "students should", "student challenge").
  * Use **"you"**, **"we"**, or objective-oriented phrasing such as **"To understand..."**, **"To learn..."**, and **"Your Task:"**.
  * Teacher/development notes must remain strictly separated from student-facing curriculum files.
* **Core Mental Anchors:**
  * *Classification:* **Apple vs. Orange** (features: color, texture $\to$ labels) $\to$ **Tumor Classification** (benign vs. malignant).
  * *Regression:* **House Price Prediction** (continuous value) $\to$ **Gene Expression / Epigenetic Age Prediction**.
  * *Clustering:* **Grouping unlabeled fruits** $\to$ **Subtype discovery in RNA-seq data**.

---

## 6. Completed Artifacts & Material Registry

| Topic / Focus | Artifact Link | Description |
|---|---|---|
| **Course Kickoff** | [Day1/Day1_Master_Kickoff_Agenda.md](Day1/Day1_Master_Kickoff_Agenda.md) | 5-step kickoff agenda & session plan |
| **Syllabus Guide** | [Day1/course_unit_details.md](Day1/course_unit_details.md) | Full 4-unit curriculum with biological analogies |
| **Career Mapping** | [Day1/career_opportunities_and_usecases.md](Day1/career_opportunities_and_usecases.md) | Industry alignment (Biopharma, Diagnostics, AgBio) |
| **Diagnostic Quiz** | [Day1/student_assessment_quiz.md](Day1/student_assessment_quiz.md) | Baseline readiness check (Python, Git, Math, Biology) |
| **Day 2 Agenda** | [Day2/Day2_Master_Agenda.md](Day2/Day2_Master_Agenda.md) | Comprehensive 5-step Day 2 master schedule & practice |
| **ML Theory Primer** | [Day2/Day2_Master_ML_Theory_Primer.md](Day2/Day2_Master_ML_Theory_Primer.md) | Visual foundations & ML vocabulary primer |
| **Decision Tool** | [Day2/Student_Biological_Problem_Questionnaire.ipynb](Day2/Student_Biological_Problem_Questionnaire.ipynb) | 5-step guided framework from biological question to ML model |

---

## 7. Active Roadmap & Next Priorities
1. **Unit 1.2:** Data Preprocessing & Sequence Encoding ($k$-mers, one-hot, scaling).
2. **Unit 1.3 & 1.4:** Regression mathematical intuition & biological application notebooks.
3. **Lab 1 & Lab 2:** Scaffolded student practical notebooks with validation checks.
