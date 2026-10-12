---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 3 — Deep Learning for Biological Data
scheduled_dates: Week 7 (Days 13 & 14)
document_type: Session Agenda
ai_tier: Full AI (Learning Aid)
---

# Sessions 13 & 14: How Neural Networks Learn & Applied Keras Workflow

---

## 1. Recap & Context

* **The Unit Arc:** In Units 1 and 2, our classical models (Linear Regression, Random Forests, PCA) relied entirely on pre-calculated, human-engineered tabular matrices. In Unit 3, we transition to **Deep Learning**, where neural networks learn hierarchical feature representations directly from raw biological measurements.
* **Day 11 Refresher:**
  * *The Artificial Neuron:* Computes a weighted sum of incoming biomarker features plus a bias, then passes through an activation gate:
    $$z = \mathbf{w}^T \mathbf{x} + b = \sum_{j=1}^{p} w_j x_j + b, \quad a = g(z)$$
  * *Activation Gates:* Sigmoid for squishing continuous scores into probabilities ($[0, 1]$); ReLU ($\max(0, z)$) for intermediate layers to enable complex, non-linear decision boundaries.
  * *Multi-Layer Architecture:* Connecting neurons into Input, Hidden, and Output layers.
* **Administrative Check-in:** Ensure all ongoing group project submissions and exercise discussions are logged directly via **GitHub Issues** on our repository.

---

## 2. Assessment & Project Check-in

During the initial practical portion of the week, we will run two parallel tracks:

### Track A: Day 10 Comprehensive Quiz Make-Up (Quiet Exam Zone)
* **Target Cohort:** Students who were absent during Session 10 and Session 11.
* **Format:** 20-minute timed, closed-book assessment under **Tier 1: No AI** conditions.
* **Resource:** [Day 10 Comprehensive Assessment Quiz](../../../assessments/day_10_comprehensive_quiz/day_10_comprehensive_quiz.md) (18 questions covering Days 1–10 synthesis).
* **Goal:** Finalize all mid-term assessment submissions for 100% of the cohort.

### Track B: Group Project Charter Sync & Keras Setup (Collaborative Studio)
* **Target Cohort:** Students who completed the quiz on Day 10.
* **Activity:**
  * Review submitted Milestone 1 Project Charters on GitHub Issues per the [Applied ML Project Guide](../../unit_02_classical_ml/applied_project_guide.md).
  * Confirm dataset selections from canonical sources (TCGA, GEO, UCI) and ensure clinical target labels ($y$) are well-defined.
  * Verify that `tensorflow` is operational in your VS Code `gcu-aiml-bioinfo` environment.

---

## 3. Theory: How Neural Networks Learn
*Assigned Reading Guide:* [3.1_how_neural_networks_learn.md](../3.1_how_neural_networks_learn.md)

We cover the complete learning mechanism as one continuous progression across our sessions:

1. **The Internal Learning Loop:**
   * Calibrating an automated fluorescence microscope: Error measurement $\to$ Sensitivity check $\to$ Corrective adjustment.
2. **Biological Framing:**
   * Cellular signal transduction cascades (MAPK pathway) mirror **Forward Propagation**.
   * Endocrine negative feedback loops (HPT axis) mirror **Backpropagation**.
3. **Forward Propagation Mechanics:**
   * Two-step transformation at each neuron: linear combination ($z$) followed by non-linear activation ($a$).
   * Tracing Patient X (*HER2*=1.5, *ESR1*=0.8) through a 2-hidden-neuron network to obtain initial predicted probability ($\hat{y} = 0.409$).
4. **Loss Functions & Quantifying Misdiagnosis:**
   * Why classification accuracy cannot guide learning (it has a derivative of zero almost everywhere).
   * **Binary Cross-Entropy (BCE):** Penalizing confident wrong answers ($-\ln(\hat{y})$) to reflect clinical diagnostic risk.
5. **Backpropagation & Credit Assignment:**
   * The "volume knob" analogy for partial derivatives ($\partial \mathcal{L} / \partial w$).
   * Applying the **Chain Rule** of calculus to link distant internal weights to the output loss referee.
6. **Gradient Descent & Optimization:**
   * Updating parameters downhill toward minimal loss: $w_{\text{new}} = w_{\text{old}} - \alpha \frac{\partial \mathcal{L}}{\partial w}$.
   * The learning rate dilemma: why $\alpha$ must be tuned to avoid divergence or stalling.
7. **Training Dynamics:**
   * The medical resident reviewing case files analogy: **Sample**, **Batch Size** ($B$), and **Epoch**.
   * Why Mini-Batch Gradient Descent ($B = 16, 32$) combined with the **Adam optimizer** is the standard in bioinformatics.
8. **Overfitting in High-Dimensional Omics ($p \gg n$):**
   * The hospital bed number analogy: memorizing patient-specific confounders vs. learning genuine disease biology.
   * Diagnosing memorization by watching Training Loss decrease while Validation Loss climbs.
9. **Regularization Defenses:**
   * **Dropout:** Randomly silencing 20–40% of hidden neurons during training to enforce genetic pathway redundancy.
   * **Early Stopping:** Halting training automatically when validation loss stops improving.
   * **Feature Scaling Invariant:** Why all biological inputs must be standardized with `StandardScaler` prior to neural network training.

---

## 4. Hands-On Practical: Applied Keras Workflow
*Interactive Laboratory Notebook:* [3.1_intro_ann_keras.ipynb](../3.1_intro_ann_keras.ipynb)  
*Aligned Practical Experiment:* [Lab 06: ANN Keras Workflow](../../../labs/lab_06_ann_keras_workflow/)

We implement the complete 4-step applied Keras workflow on our breast cancer biomarker cohort:

* **Step 0: Environment Setup & Reproducible Imports:** Initializing TensorFlow/Keras and fixing random seeds (`seed=42`).
* **Step 1: Biological Toy Dataset & Partitioning:** Simulating 100 biopsies (*HER2* vs. *ESR1*) and creating a leak-free 80/20 train/test split.
* **Step 2: Defining the Architecture:** Building a $2 \to 2 \to 1$ MLP in Keras; dissecting the parameter summary to verify the exact $6 + 3 = 9$ trainable parameters.
* **Step 3: Untrained Baseline:** Passing Patient X through the uncalibrated model to observe the random guess baseline ($P \approx 79.6\%$).
* **Step 4: Compiling the Model:** Specifying `optimizer='adam'`, `loss='binary_crossentropy'`, and `metrics=['accuracy']`.
* **Step 5: Training (`model.fit`):** Running the 50-epoch calibration loop with batch size 16 and held-out validation tracking.
* **Step 6: Visualizing Training Trajectory:** Plotting training vs. validation loss curves and accuracy trajectories.
* **Step 7: Visualizing the Decision Boundary:** Rendering a 2D contour plot over *HER2* and *ESR1* space showing the non-linear threshold boundary ($P = 0.50$).
* **Step 8: Formal Test Evaluation:** Running `model.evaluate()` on unseen test patients and re-evaluating Patient X ($79.6\% \to 91.6\%$ confidence).
* **Step 9: Adding Regularization:** Incorporating `layers.Dropout(0.25)` to build a regularized multi-layer architecture.
* **Step 10: Interactive Sandbox & Challenge:** Experimenting with layer depths, neuron counts, batch sizes, and learning rates.

---

## 5. Takeaways & Next Steps

* [ ] **Takeaway 1:** NA (In-class focus on mastering Keras fundamentals; no additional standalone takeaway assigned).
* [ ] **Project Milestone 1 Follow-up:** Review instructor feedback on your Group Project Charter on GitHub Issues, confirm your raw dataset files from TCGA/GEO/UCI, and begin outlining your data preprocessing scripts.
