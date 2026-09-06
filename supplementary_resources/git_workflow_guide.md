# Version Control with Git & GitHub: A Practical Crash Course for Computational Biology

*A comprehensive, practical reference for managing bioinformatics scripts, tracking machine learning experiments, and collaborating reproducibly.*

---

## 1. Why Version Control Matters in Bioinformatics & Machine Learning

In computational biology and biomedical data science, research workflows evolve rapidly. Without a formal version control system, projects quickly descend into chaotic file naming:

```
❌ The Dangerous Old Way:
├── rnaseq_analysis.py
├── rnaseq_analysis_v2.py
├── rnaseq_analysis_final.py
├── rnaseq_analysis_final_CORRECTED.py
└── rnaseq_analysis_final_USE_THIS_ONE.py
```

### Key Benefits for Your Work:
1. **Total Reproducibility:** Every scientific finding, trained ML model, and figure can be traced back to the exact line of code and commit hash that produced it.
2. **Fearless Experimentation:** You can test a new hyperparameter tuning algorithm on a dedicated branch without breaking your working baseline pipeline.
3. **Collaboration & Code Review:** Multiple bioinformaticians can work on sequence processing, feature extraction, and neural network training simultaneously without overwriting each other's work.
4. **Audit Trail for Scientific Publications:** Journals and grant agencies increasingly require public GitHub repositories accompanying published bioinformatics tools and models.

---

## 2. The Git Mental Model: The Three Local Trees + Remote

Git tracks snapshots of your files over time. Understanding the four operational areas is key to mastering Git:

```
┌─────────────────┐      git add       ┌─────────────────┐     git commit     ┌─────────────────┐      git push       ┌─────────────────┐
│ Working Tree    │ ─────────────────> │ Staging Area    │ ─────────────────> │ Local Repo      │ ──────────────────> │ Remote (GitHub) │
│ (Modified Files)│ <───────────────── │ (Index)         │                    │ (Committed HEAD)│ <────────────────── │ (Origin)        │
└─────────────────┘    git restore     └─────────────────┘                    └─────────────────┘      git pull       └─────────────────┘
```

* **Working Directory:** The actual files you are currently editing on your computer.
* **Staging Area (Index):** The draft staging area where you gather specific changes you want to include in your next snapshot.
* **Local Repository (`.git`):** The permanent historical record of all committed snapshots on your local machine.
* **Remote Repository (GitHub):** The cloud-hosted copy of your repository used for backup and team collaboration.

---

## 3. Initial Configuration (Run Once)

Before making your first commit, configure your identity so your contributions are correctly attributed:

```bash
# Set your name and email (use the same email registered with GitHub)
git config --global user.name "Your Name"
git config --global user.email "your.email@university.edu"

# Set the default branch name to main
git config --global init.defaultBranch main

# Verify your configuration
git config --list
```

---

## 4. Daily Core Workflow: Step-by-Step

### Step A: Starting or Cloning a Project
```bash
# Scenario 1: Initialize a brand-new local repository
cd my_bioinformatics_project/
git init

# Scenario 2: Clone an existing remote repository from GitHub
git clone https://github.com/YourUsername/bioinformatics-ml-curriculum.git
cd bioinformatics-ml-curriculum/
```

### Step B: Checking Status & Inspecting Changes
```bash
# Check which files have been created, modified, or staged
git status

# Inspect the exact line-by-line differences before staging
git diff

# Inspect staged changes vs. the last commit
git diff --staged
```

### Step C: Staging & Committing (Creating Snapshots)
```bash
# Stage a specific file
git add preprocess_rnaseq.py

# Stage all modified and new files in the current folder
git add .

# Save the snapshot with a clear, descriptive message in the imperative mood
git commit -m "Add log2 normalization and missing value imputation to RNA-seq pipeline"
```

### Step D: Synchronizing with GitHub (Pushing & Pulling)
```bash
# Link a local repository to a new empty GitHub repository (first time only)
git remote add origin https://github.com/YourUsername/my_bioinformatics_project.git
git branch -M main
git push -u origin main

# Subsequent pushes (after making new commits)
git push

# Fetch and integrate the latest changes made by collaborators from GitHub
git pull origin main
```

---

## 5. Branching & Isolated Development

Branches allow you to build new features, test different ML architectures, or fix bugs in complete isolation from the stable `main` branch.

```
(main)           C1 ─── C2 ──────────── C5 ─── C6 (merged main)
                         \             /
(feature/xgboost)         C3 ─── C4 ──
```

### Essential Branching Commands:
```bash
# Create and switch to a new feature branch
git switch -c feature/xgboost-classification
# (Older equivalent: git checkout -b feature/xgboost-classification)

# List all local branches (the active branch is marked with an asterisk *)
git branch

# Switch back to the main branch
git switch main

# Merge your completed feature branch into main
git merge feature/xgboost-classification

# Delete the feature branch after successful merge
git branch -d feature/xgboost-classification
```

---

## 6. The Critical `.gitignore` for Biological Data & Machine Learning

**Rule of Thumb:** Never commit large raw data files, sensitive clinical credentials, or heavy temporary binaries into Git. Git is designed for text/code; storing multi-gigabyte genomic files will bloat your repository and cause GitHub push rejections (GitHub limits individual files to 100MB).

Create a file named `.gitignore` in your repository root:

```gitignore
# ==========================================
# Biological Raw Data & Sequencing Formats
# ==========================================
*.fastq
*.fq
*.bam
*.sam
*.vcf
*.vcf.gz
*.h5ad
*.rds
data/raw/
data/processed/

# ==========================================
# Heavy Machine Learning Model Weights
# ==========================================
*.pt
*.pth
*.h5
*.keras
*.onnx
*.pkl
*.joblib
models/checkpoints/

# ==========================================
# Python & Environment Artifacts
# ==========================================
__pycache__/
*.py[cod]
*$py.class
.ipynb_checkpoints/
.env
.venv/
env/
venv/

# ==========================================
# OS & Editor Files
# ==========================================
.DS_Store
Thumbs.db
.vscode/
.idea/
```

---

## 7. Inspecting History & Undoing Mistakes Safely

### Viewing History:
```bash
# View compact commit history with graph structure
git log --oneline --graph --decorate -n 10

# View history of changes for a specific file
git log -p -2 preprocess_rnaseq.py
```

### Undoing Mistakes:
```bash
# 1. Unstage a file you accidentally added (keeps your edits intact)
git restore --staged mistaken_file.py

# 2. Discard all uncommitted local modifications in a file (revert to last commit)
git restore modified_file.py

# 3. Amend the most recent commit message or add forgotten staged files
git commit --amend -m "Updated commit message"

# 4. Safely undo an older public commit by creating a new inverse commit
git revert <commit_hash>
```

---

## 8. Summary Command Cheat Sheet

| Command | What It Does |
|---|---|
| `git init` | Initialize a new local Git repository in the current folder |
| `git clone <url>` | Download a remote repository and its full history |
| `git status` | Show changed, staged, and untracked files |
| `git diff` | Show exact line additions/deletions not yet staged |
| `git add <file>` | Add changes from working tree to the staging area |
| `git commit -m "msg"` | Permanently record staged changes as a new snapshot |
| `git log --oneline` | View compact timeline of past commits |
| `git switch -c <name>` | Create and switch to a new branch |
| `git merge <name>` | Combine changes from another branch into your current branch |
| `git pull origin <branch>` | Download and merge changes from GitHub to your local repo |
| `git push origin <branch>` | Upload your local commits to GitHub |

---

## 9. Curated Resources for Further Learning

To deepen your mastery of version control, explore these resources:

1. **[Pro Git Book (by Scott Chacon and Ben Straub)](https://git-scm.com/book/en/v2)**  
   *The definitive, official, and completely free textbook covering Git from fundamentals to advanced internal plumbing.*
2. **[Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/)**  
   *The gold-standard tutorial designed specifically for scientific researchers, bioinformaticians, and computational scientists.*
3. **[Learn Git Branching (Interactive Visual Sandbox)](https://learngitbranching.js.org/)**  
   *An interactive visual browser tutorial that lets you drag, drop, and visualize branch merges, rebases, and cherry-picks.*
4. **[GitHub Skills Hands-On Modules](https://skills.github.com/)**  
   *Interactive, repository-based learning courses hosted directly within GitHub.*
5. **[Oh Shit, Git!?! (Troubleshooting Guide)](https://ohshitgit.com/)**  
   *Plain-English solutions for rescuing your work when you get stuck or make a mistake in Git.*
