---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
unit: Unit 3 — Deep Learning for Biological Data & Applied Practicals
scheduled_dates: Week 9 (Day 17)
document_type: Session Agenda
ai_tier: Full AI (Learning Aid)
---

# Session 17: Intro to Agentic Coding & Lab Exercise 01 Wrap-Up

**Course Code:** `02BMSBI24365` — AI and ML in Bioinformatics  
**Primary Computing Environment:** Visual Studio Code (`gcu-aiml-bioinfo` Conda environment)  
**Primary Theory Guide:** [3.4_intro_to_agentic_coding.md](../3.4_intro_to_agentic_coding.md)  
**Interactive Notebook:** [lab_01_binary_classification_pipeline.ipynb](../../../labs/lab_01_binary_classification_pipeline/lab_01_binary_classification_pipeline.ipynb)  

---

## 📌 Session Roadmap

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      DAY 17 INSTRUCTIONAL ROADMAP                      │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Recap & Synthesis                                                   │
│    • Review Lab 01 PAM50 pipeline & zero data leakage invariant        │
│ 2. Dual-Track Cohort Split                                             │
│    • Track A: Day 10 Comprehensive Quiz Make-Up (20 min, Tier 1)       │
│    • Track B: Lab 01 in-class debugging & GitHub issues intake         │
│ 3. Methodological Briefing: Intro to Agentic Coding                    │
│    • The Coding Evolution: Manual → Web Chatbots → In-IDE Agents       │
│    • In-editor tool stack: Copilot, Claude Code, Antigravity           │
│    • Autonomous agent ecosystems: OpenClaw, Hermes, Pi, Muse           │
│ 4. Hands-On Sprint: In-IDE Agentic Workflow & Lab 01 Finalization      │
│    • Live demonstration: Context-aware prompting inside VS Code        │
│    • Finalize Stages 9–10 (Benchmark synthesis & 5-gene panel)         │
│ 5. Takeaways & Submission                                              │
│    • Clean notebook (`nbstripout`) & open GitHub Issue                 │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Recap & Synthesis

* **Pipeline Recap:** On Day 16, we implemented Stages 1–8 of the TCGA-BRCA classification pipeline, establishing baseline performance for Logistic Regression, Random Forest, and a Keras ANN.
* **Methodological Invariants:**
  * Scaling transformers (`StandardScaler`) must be fitted exclusively on `X_train` to prevent data leakage.
  * Decision threshold shifting ($\tau$) tunes model sensitivity to guard against catastrophic False Negatives in Basal-like tumors.

---

## 2. Assessment & Lab Intake Split

### Track A: Day 10 Comprehensive Quiz Make-Up (Quiet Exam Zone)
* **Target Cohort:** Students absent during Days 10–16.
* **Format:** 20-minute closed-book written quiz under **Tier 1: No AI** conditions.
* **Resource:** [Day 10 Comprehensive Assessment Quiz](../../../assessments/day_10_comprehensive_quiz/day_10_comprehensive_quiz.md).

### Track B: Lab 01 Intake & In-Class Debugging (Collaborative Studio)
* **Target Cohort:** Students who have completed the Day 10 quiz.
* **Activity:** Live code review, diagnostic verification, and intake assistance for Lab 01 project charters on GitHub Issues.

---

## 3. Methodological Briefing: Introduction to Agentic Coding
*Assigned Primer:* [3.4_intro_to_agentic_coding.md](../3.4_intro_to_agentic_coding.md)

* **The Four Coding Generations:**
  1. *Manual:* Syntax memorization and documentation search.
  2. *Web Chatbots (ChatGPT / Web Claude):* Copy-pasting snippets across browser tabs (loss of project context, hallucinated imports).
  3. *In-IDE Agents (GitHub Copilot, Claude Code, Antigravity):* Direct file-tree and terminal awareness, inline debugging, zero copy-paste friction.
  4. *Autonomous Agent Frameworks (OpenClaw, Hermes, Pi, Muse):* Multi-tool orchestration, iterative planning, and automated debugging.
* **Beyond the Chatbot (Anatomy of a True Coding Agent):**
  * *Model Context Protocol (MCP):* Direct queries to external biological repositories (NCBI, UniProt, S3) without manual API scripts.
  * *Skills & Workflows:* Reusable domain recipes (e.g., zero-leakage enforcement, automated QC).
  * *Plugins & Tool Execution:* Integrated linters, compilers, and bioinformatics CLI tools.
  * *State Rewind & Checkpoints:* Time-travel rollbacks to safely explore architectural variations.
  * *Closed-Loop Self-Correction:* Autonomous debugging loops ($\text{Plan} \to \text{Execute} \to \text{Inspect Stderr} \to \text{Patch}$).
* **Why In-IDE Context Matters:** Eliminating manual copy-pasting ensures AI assistants understand your exact Conda environment packages, file paths, and dataset dimensions ($n \times p$).

---

## 4. Hands-On Practical: In-IDE AI Workflow & Lab 01 Sprint

Work in [lab_01_binary_classification_pipeline.ipynb](../../../labs/lab_01_binary_classification_pipeline/lab_01_binary_classification_pipeline.ipynb):

1. **In-IDE Prompting Demonstration:** Leverage context-aware prompts directly within VS Code to refactor pipeline functions without opening external browser windows.
2. **Stage 9 (Benchmark Synthesis):** Compile the comparative performance table across Logistic Regression, Random Forest, and Keras ANN with ROC-AUC curve overlays.
3. **Stage 10 (Student Challenge):** Train and evaluate the minimal 5-gene point-of-care signature (*FOXA1*, *CDC20*, *MELK*, *KIF2C*, *EXO1*), comparing diagnostic retention against the full 60-gene panel.

---

## 5. Takeaways & Deliverables

* [ ] Clean execution outputs using `pre-commit run --all-files` (`nbstripout`).
* [ ] Open a **New Issue** on the course repository with your model comparison table, ROC curve plot, and 3-sentence biological interpretation.
* [ ] Read [3.4_intro_to_agentic_coding.md](../3.4_intro_to_agentic_coding.md) to prepare for the upcoming mid-November Agentic Coding & Vibe Coding Workshop.
