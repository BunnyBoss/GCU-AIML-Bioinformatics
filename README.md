# Machine Learning & AI for Bioinformatics

**Course Code:** `02BMSBI24365`  
**Institution:** Garden City University (GCU), School of Sciences, Department of Life Sciences  
**Program:** M.Sc. Bioinformatics (Semester III / Year 2)  
**Format:** 12-Week Master Curriculum + 10 Hands-on Computer Laboratory Practicals  

---

## Course Description & Objectives

Biological data has undergone an exponential explosion in volume, dimensionality, and heterogeneity—ranging from high-throughput transcriptomics ($20,000+$ gene expression features) and whole-genome variant call formats (VCF) to high-resolution histopathological imaging and single-cell sequencing. This course bridges molecular biology and modern computational intelligence, equipping you with the statistical learning and deep learning methodologies required to extract genuine biological signal from complex multi-omics data.

### Course Objectives

By following this curriculum, you will:

* **Master AI & Machine Learning Algorithms:** Acquire deep theoretical and practical knowledge of diverse AI and machine learning algorithms—including supervised classification, continuous regression, unsupervised clustering, and dimensionality reduction—specifically tailored to address bioinformatics-specific challenges.
* **Preprocess & Integrate Heterogeneous Biological Data:** Learn to clean, preprocess, normalize, and integrate diverse biological data sources, such as genomic sequences, transcriptomic gene expression profiles, and protein macromolecular structures, optimizing them for computational intelligence pipelines.
* **Engineer Biologically Informative Features:** Develop rigorous feature selection and engineering skills to identify relevant signals within high-dimensional biological data and generate informative representations (such as $k$-mer frequency profiles and one-hot sequence encodings) that enhance model performance for biomarker identification, variant prioritization, and disease prediction.
* **Interpret Models & Extract Biological Insights:** Master modern evaluation frameworks and model interpretation techniques (including Explainable AI with SHAP and LIME) to critically assess model performance, prevent data leakage, and extract biologically meaningful, clinically actionable insights for applications in translational research, personalized medicine, and drug discovery.

---

## Curriculum Structure

The course is organized into four core academic units:

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

## Repository Directory Guide

This repository contains all student materials needed for lectures, reading, and computer labs:

* [units/](units/): Theoretical curriculum modules, topic guides, and instructional notebooks.
  * [units/unit_01_foundations/](units/unit_01_foundations/): Mathematical foundations, biological data encoding ($k$-mers, one-hot), and continuous outcome regression.
  * [units/unit_02_classical_ml/](units/unit_02_classical_ml/): Decision Trees, Random Forests, Support Vector Machines, $K$-Means, Hierarchical Clustering, PCA, and Cross-Validation.
  * [units/unit_03_deep_learning/](units/unit_03_deep_learning/): Neural network mechanics, Backpropagation, Keras/TensorFlow, 2D-CNNs for biomedical imaging, 1D-CNN/LSTMs for sequences, and Transformer foundation models.
  * [units/unit_04_ai_applications/](units/unit_04_ai_applications/): Pan-cancer survival analysis, sequence motif discovery, protein family classification, and SHAP/LIME biomarker attribution.
* [labs/](labs/): 10 graded laboratory practicals featuring guided walkthroughs, biological datasets, and student challenge exercises.
* [datasets/](datasets/): Standardized biological benchmark datasets (Breast Cancer Wisconsin, TCGA RNA-seq, NCBI GEO expression arrays, histone ChIP-seq profiles) and reproducible fetching scripts.
* [assessments/](assessments/): Baseline diagnostic quiz, continuous evaluation rubrics, lab practical examination templates, and capstone milestone criteria.
* [supplementary_resources/](supplementary_resources/): Step-by-step guides for Conda/Mamba virtual environments, Git/GitHub workflows, VS Code setup, and command-line tooling.

---

## Getting Started & Environment Setup

**Default Development Environment:** Visual Studio Code (VS Code) is the uniform platform used across all lectures, notebooks, and lab practicals in this course.

### 1. Prerequisites
Ensure you have installed:
* [Visual Studio Code](https://code.visualstudio.com/)
  * Install the **Python** (`ms-python.python`) and **Jupyter** (`ms-toolsai.jupyter`) extensions in VS Code.
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Mambaforge](https://github.com/conda-forge/miniforge) (Python 3.10+ recommended)
* [Git](https://git-scm.com/)

### 2. Clone the Repository & Open in VS Code
```bash
git clone https://github.com/BunnyBoss/GCU-AIML-Bioinformatics.git
cd GCU-AIML-Bioinformatics
code .
```

### 3. Create the Conda Environment
Open the integrated terminal in VS Code (`Ctrl+\`` or `Cmd+\``) and run:
```bash
# Create dedicated environment
conda create -n gcu-aiml-bioinfo python=3.10 -y
conda activate gcu-aiml-bioinfo

# Install core scientific and machine learning dependencies
conda install -c conda-forge -c bioconda numpy scipy pandas scikit-learn matplotlib seaborn ipykernel biopython -y

# Register environment with Jupyter kernel
python -m ipykernel install --user --name gcu-aiml-bioinfo --display-name "Python (gcu-aiml-bioinfo)"

# Installation of deep learning and interpretability packages will be discussed in future sessions

```

### 4. Enable Notebook Cleanliness (Pre-commit Hooks)
To keep the repository lightweight and prevent large data outputs or cached image plots from bloating your submissions:
```bash
pip install pre-commit nbstripout
pre-commit install
```

### 5. Running Notebooks in VS Code
1. Open any notebook (e.g., [units/unit_01_foundations/1.1_intro_ml_in_bioinformatics.ipynb](units/unit_01_foundations/1.1_intro_ml_in_bioinformatics.ipynb) or your assigned lab in [labs/](labs/)) directly in the VS Code file explorer.
2. In the top right corner of the notebook editor, click **Select Kernel** $\rightarrow$ **Python Environments...** $\rightarrow$ choose **`gcu-aiml-bioinfo`**.
3. Run cells interactively using `Shift+Enter`.

---

## AI Assistance Policy & Tier Framework

To help you learn effectively and responsibly in the era of artificial intelligence, every notebook (`.ipynb`) and guide (`.md`) in this repository declares an **AI Tier** in its header/frontmatter (`ai_tier`). This specifies the permissible level of AI assistance (e.g., ChatGPT, Claude, GitHub Copilot) for that specific task:

| Tier | Policy Label | What It Means for You | Typical Course Materials |
|:---:|---|---|---|
| **1** | **Tier 1: No AI** | Complete the task entirely unaided. No AI explanation, code generation, or hint prompting. | Midterm & final practical exams, timed skill checks |
| **2** | **Tier 2: AI Planning Only** | You may use AI to brainstorm approaches, outline architectures, or clarify errors—but **not** to write the actual code or analytical solution. | Early-to-mid semester laboratory practicals, graded homework |
| **3** | **Tier 3: AI Collaboration (Disclosed)** | You may use AI tools throughout your analysis, but you **must** disclose where and how they were used in your submission notes. | Advanced later-semester labs once core skills are established |
| **4** | **Tier 4: Full AI + Reflection** | Full AI assistance is permitted, but you **must** submit a short reflection detailing what the AI generated and where you corrected or overrode it. | Capstone project, open-ended research workflows |
| **—** | **Full AI (Learning Aid)** | Non-assessed learning material. You may freely use AI to explain concepts, generate extra biological examples, or quiz yourself. | Theory lecture guides (`units/`), self-check quizzes, tutorials |

*Always check the `ai_tier` declaration at the top of any assigned notebook or assessment before beginning your work.*

---

## Academic Integrity & Code Expectations
* **Authentic Learning:** All code implementations, analysis summaries, and capstone submissions must adhere strictly to the declared `ai_tier` for that deliverable.
* **Collaboration Policy:** Collaborative conceptual discussions of algorithms are encouraged; however, sharing direct code solutions or unpermitted AI-generated outputs violates course policy.

---

## Contact & Institutional Information
* **Course Coordinator:** Faculty of Life Sciences & Bioinformatics, Garden City University
* **Course Syllabus Reference:** [curriculum.md](supplementary_resources/curriculum.md)
* **License:** Educational Courseware License — Garden City University (GCU)
