---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 1 — Foundations of Machine Learning for Bioinformatics
document_type: Session Agenda
---

# 📅 Day 3 Agenda: Biological Problem Formulation & Data Preprocessing

Welcome to Session 3. Today, we will transition from the theoretical landscape of Machine Learning into the practical mechanics of formulating biological problems and preprocessing raw data.

## 1. Recap
* **Immediate Recap (Day 02):** A review of the 4-step universal ML workflow: Dataset preparation, Model selection, Train, Evaluate.
* **Referenced Materials:**
  * Previous Session Notebook: [1.1_intro_ml_in_bioinformatics.ipynb](../1.1_intro_ml_in_bioinformatics.ipynb)
  * Unit Syllabus Milestone: [curriculum.md](../../../supplementary_resources/curriculum.md)
* **Clarification:** We will clarify the regression line visualization axes and scaling observed in the Day 2 notebook.

## 2. Review of Takeaway Exercises
* **Repository Introduction:** An introduction to the new permanent GitHub repository using the root [README.md](../../../README.md) to demonstrate where units, labs, assessments, and datasets are housed.
* **The Golden Triad Workflow:** A quick walkthrough of how Conda, VS Code, and Git work in combination to handle the entire curriculum, guided by [repo_and_workflow_walkthrough.md](../../../supplementary_resources/repo_and_workflow_walkthrough.md).
* **Setup Check-in:** Ensuring all local Python and Conda environments are correctly configured.

## 3. Theory (The 5-Stage Learning Ladder)
* **Topic A: Finishing Problem Formulation (Rollover)**
  * *Interactive Theory Session.*
  * Live conceptual walk-through of translating biological questions into Classification, Regression, or Clustering tasks using the breast tissue biopsy example in [problem_formulation_tool.ipynb](../problem_formulation_tool.ipynb).
* **Topic B: Data Preprocessing & Feature Engineering (Unit 1.2)**
  * *Theory Primer:* [1.2_data_preprocessing_primer.md](../1.2_data_preprocessing_primer.md)
  * We will introduce the 5 core categories of raw data problems using general vs. biological examples.
  * *Structural:* Missing values (NaN) and technical dropouts.
  * *Dimensionality:* Zero-variance features ($p \gg n$).
  * *Representation:* Translating text categories into mathematical tensors via One-Hot Encoding.

## 4. Hands-On Practical & Deliverables
* **Primary Computing Environment:** Visual Studio Code (`gcu-aiml-bioinfo` Conda kernel)
* **Part 4A: Data Preprocessing & Feature Engineering (Unit 1.2)**
  * *Interactive Notebook:* [1.2_data_preprocessing_part_a.ipynb](../1.2_data_preprocessing_part_a.ipynb)
  * *Walkthrough:* We will use simple 'Messy House Prices' and 'Messy Fruits' datasets to learn the preprocessing mechanics safely before applying them to high-dimensional biology.
  * Demonstrating `SimpleImputer` for missing values, `VarianceThreshold` for zero-variance filtering, and One-Hot Encoding (`pd.get_dummies`).
* **📌 Takeaway Exercises & Deliverables for Day 4:**
  - [ ] Complete the 4 problem formulation scenarios (Epigenetic Clock, AMR, Chemotherapy, Viral subtypes) located at the bottom of [problem_formulation_tool.ipynb](../problem_formulation_tool.ipynb).

