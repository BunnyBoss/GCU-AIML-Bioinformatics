# Bioinformatics Curriculum Workflow & Repository Guide

## 1. Introduction to the New GitHub Repository

We have migrated from our temporary repository to a dedicated, unified GitHub repository that will act as our Single Source of Truth for the entire course. 

We will walk through the [README.md](../../README.md) at the root of this repository, which outlines:
*   **Units (`units/`)**: Where all theoretical concepts and interactive Jupyter notebooks (like our Machine Learning primers) are housed.
*   **Labs (`labs/`)**: Practical, hands-on lab experiments for you to complete.
*   **Assessments (`assessments/`)**: Quizzes and project evaluations.
*   **Datasets (`datasets/`)**: Benchmark biological datasets (e.g., TCGA, GEO) we will use throughout the course.
*   **Supplementary Resources (`supplementary_resources/`)**: Additional guides and setup instructions.

This repository will be the central hub where you pull the latest materials each week.

---

## 2. The Golden Triad: Conda + VS Code + Git

To successfully navigate the bioinformatics curriculum, we use three industry-standard tools in combination. Here is a quick walkthrough of how they integrate:

### A. Git & GitHub (Version Control & Distribution)
*   **The Role:** Git acts as our course delivery system and your project snapshot tool.
*   **The Workflow:** 
    *   `git pull` at the start of each session to fetch new lecture notebooks and datasets.
    *   `git commit` to save your progress on lab experiments locally.
    *   `git push` (if working on your own forks/branches) to submit assessments.

### B. Conda (Environment Management)
*   **The Role:** Conda ensures that your Python packages (Scikit-learn, TensorFlow, BioPython) match exactly what is required for the course, preventing "it works on my machine" errors.
*   **The Workflow:**
    *   You activate the `gcu-aiml-bioinfo` environment before starting any work.
    *   This provides a sandbox containing Python 3.10 and all essential bioinformatics libraries.

### C. Visual Studio Code (The Integrated Workspace)
*   **The Role:** VS Code ties Git and Conda together into a single, unified interface.
*   **The Workflow:**
    *   Open the cloned repository folder in VS Code.
    *   Use the integrated terminal to run Conda commands or Git commands.
    *   Open `.ipynb` files directly; VS Code will automatically detect your Conda environment and allow you to run data preprocessing pipelines and ML models seamlessly.

By mastering this triad, you mirror the exact environment used by professional bioinformaticians and machine learning engineers worldwide.
