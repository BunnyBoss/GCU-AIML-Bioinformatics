---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 3 — Deep Learning for Biological Data
scheduled_dates: Week 6 / Lecture 1 (Day 11)
document_type: Session Agenda
ai_tier: Full AI (Learning Aid)
---

# Session 11: Introduction to Artificial Neural Networks & Applied ML Project Consultation

---

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       DAY 11 INTEGRATED ROADMAP                                        │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Recap & Admin Check-in (10 min)                                                                     │
│    • High-Level Synthesis of Units 1 & 2: The Classical ML Landscape (Supervised vs. Unsupervised)     │
│    • Top-level recap: Classification, Regression, Clustering, and Dimensionality Reduction             │
│    • Conceptual bridge: From tabular feature workflows to Deep Learning representation learning       │
│    • Administrative Check-in: Brief reminder on GitHub Issues submission tracking                      │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Review of Takeaways & Day 10 Quiz Debrief (5 min)                                                   │
│    • Final reminder: Day 10 practical deliverables must be submitted max by tomorrow                   │
│    • Quiz acknowledgment: Good job to all attendees                                                    │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Theory — Topic A: Introduction to Artificial Neural Networks (35–40 min)                            │
│    • The Bridge: Why Classical ML hits a wall (The Dog/Cat paradox & the Biological "Tabular Trap")    │
│    • End-to-End Representation Learning & Hierarchical Feature Abstraction                             │
│    • Modeling a Single Decision: The Bengaluru Groundnut Fair (Kadalekai Parishe) Intuition Hook       │
│    • Biological Counterpart: Dendrites, Synapses, Soma, and Axon Firing                                │
│    • Mathematical Formalization: The Artificial Neuron (Score = wᵀx + b) & Day 10 Aha Moment           │
│    • The Power of Matrices: Dot Products, 20,000 Gene Panels, and GPU Parallelization                  │
│    • Converting Scores to Decisions: Sigmoid squishing and Activation Functions (ReLU)                 │
│    • Stacking Sub-Decisions: Building the Architecture (Input, Hidden, Output Layers)                  │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. Applied Session — Topic B: Differentiated Dual Tracks (30–40 min)                                   │
│    • TRACK A: Day 10 Make-Up Quiz (for absent students)                                                │
│    • TRACK B: End-to-End Project Consultation & Dataset Selection (for quiz completers)                │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Recap

* **Pre-Session Administrative Check-in (GitHub Issues):**
  * Reminder: Please submit any pending takeaway assignments (such as the Day 10 deliverables) directly via **GitHub Issues** in the browser to maintain an auditable portfolio.
* **Top-Level Synthesis (Units 1 & 2 Structural Overview):**
  * **Supervised Learning** (Learning driven by ground-truth target labels, $y$):
    * *Classification:* Categorizing samples into discrete biological states (e.g., Healthy vs. Diseased, Responder vs. Non-Responder).
    * *Regression:* Predicting continuous numerical realities (e.g., survival time in months, drug concentration, biological age).
  * **Unsupervised Learning** (Discovering hidden structure purely from unannotated input features, $\mathbf{X}$):
    * *Clustering:* Finding natural, undiscovered groupings and stratifications in the data.
    * *Dimensionality Reduction:* Compressing high-dimensional feature spaces down to their most informative axes.
* **The Conceptual Bridge to Unit 3 (Deep Learning):**
  * Over the first 10 days, the entire classical machine learning workflow relied on a single common denominator: **human-engineered tabular matrices**. Every algorithm we studied (Linear Regression, PCA, Random Forests) required neatly packaged, pre-calculated columns of numerical features. 
  * *The Question for Today:* What happens when the biological data is completely raw, massive, and unstructured (like whole-slide imaging or complete genome sequences)? This constraint marks the transition into **Deep Learning**.

---

## 2. Review of Takeaway Exercises & Assessment Debrief

* **Review of Day 10 Practical Deliverable:**
  * As the majority of the cohort is finalizing their Day 10 practical deliverables (Wisconsin Diagnostic Breast Cancer Classifier), we will skip a deep-dive review today.
  * **Final Reminder:** All pending Day 10 practical deliverables must be submitted via GitHub Issues maximum by tomorrow.
* **Day 10 Comprehensive Quiz Debrief:**
  * Congratulations and good job to everyone who completed the comprehensive Synthesis Quiz on Day 10!

---

## 3. Theory — Topic A: Introduction to Artificial Neural Networks (ANNs)
*Assigned Primer: [3.1_neural_networks_primer.md](../3.1_neural_networks_primer.md)*

We will step through the core conceptual foundations of Artificial Neural Networks:
1. **The Bridge — Why Classical Machine Learning Hits a Wall:** Contrasting human-engineered tabular features with raw, unstructured biological data to illustrate the critical bottleneck of classical algorithms.
2. **The Solution — End-to-End Representation Learning:** How complex models can autonomously learn hierarchical features directly from raw data without manual feature extraction.
3. **From Biology to Math — Modeling a Single Decision:** Framing a simple binary decision based on weighted inputs and a baseline bias to build intuition on how an artificial neuron decides to "fire".
4. **The Biological Neuron Counterpart:** Mapping the conceptual components of the numerical decision directly to human neurobiology (Dendrites, Synapses, Soma, and Axon).
5. **The Mathematics of the Artificial Neuron:** Dissecting the linear weighted sum equation and demonstrating its exact equivalence to the Logistic Regression model we built in Unit 2.
6. **The Power of Matrices:** Understanding how vectorizing millions of inputs and weights into dot products enables massive parallelization on modern GPUs.
7. **Converting Scores to Decisions — Activation Functions:** How continuous mathematical scores are squished into explicit final probabilities and decisions using activation gates (like Sigmoid and ReLU).
8. **Stacking Sub-Decisions — Building the Network Architecture:** Connecting individual neurons into distinct Input, Hidden, and Output layers to form a complete Deep Neural Network capable of complex representation learning.

---

## 4. Hands-On Practical & Applied Session — Topic B: Differentiated Dual Tracks

During the second half of the session, the lab will split into two concurrent tracks based on your Day 10 attendance.

### Track A: Day 10 Comprehensive Synthesis Quiz Make-Up
* **Target Cohort:** Students absent during Session 10.
* **Action:** You will take the 20-minute make-up [Day 10 Comprehensive Quiz](../../../assessments/day_10_comprehensive_quiz/day_10_comprehensive_quiz.md) under strict Tier 1 (No AI), closed-book exam conditions.

### Track B: Interactive Live Dataset Selection & End-to-End Project Workshop
* **Target Cohort:** Students who have already completed the Day 10 Quiz.
* **Action:** We will conduct an interactive workshop covering the 8-stage Applied ML Project blueprint, vetting datasets, and discussing the canonical sources for bioinformatics data.
* **Project Reference Guide:** Please refer to the [Applied ML Project: Dataset Selection & Pipeline Blueprint](../../unit_02_classical_ml/applied_project_guide.md) to review the requirements and rubrics for your milestone submission.

---

## 5. Takeaway Exercises & Deliverables for Day 12

* [ ] **Universal Deliverable (All Students - Track A & Track B): Project Milestone 1 — 1-Page Project Charter:**
  * Submit a formal Project Charter via GitHub Issues detailing your clinical objectives, dataset provenance, problem formulation, preprocessing strategy, and candidate models.
  * *Note for Track A Students:* Because you will be taking the make-up quiz during the dataset workshop, you are responsible for syncing up with your Track B peers after class to learn exactly what steps are required and how to vet your datasets for this charter submission!
* [ ] **Universal Reading Preparation for Day 12:**
  * Read [3.1_neural_networks_primer.md](../3.1_neural_networks_primer.md).