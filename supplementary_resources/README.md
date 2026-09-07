# Supplementary Computational Resources & Tooling Guides

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  

---

## Overview

Modern bioinformatics requires both strong algorithmic knowledge and proficient software engineering habits. This folder provides technical guides, environment specifications, and developer cheat-sheets to support your computational work.

---

## Guides in this Directory

| Guide | Target Topic | Key Skills & Outcomes |
|---|---|---|
| [conda_environment_guide.md](conda_environment_guide.md) | **Conda & Mamba Environments** | Creating reproducible virtual environments, handling package channel priority (`conda-forge`, `bioconda`), managing dependencies, and resolving conflicts. |
| [git_workflow_guide.md](git_workflow_guide.md) | **Git & GitHub Workflows** | Git version control fundamentals, repository cloning, branching, staging, pre-commit hooks (`nbstripout`), and remote collaboration. |

---

## Quick Reference Commands

### 1. Conda Environment Management
```bash
# Create dedicated environment
conda create -n gcu-aiml-bioinfo python=3.10 -y

# Activate environment
conda activate gcu-aiml-bioinfo

# Export exact environment for reproducible sharing
conda env export --no-builds > environment.yml

# Recreate environment from specification file
conda env create -f environment.yml
```

### 2. Git & Notebook Cleanliness
```bash
# Check status before committing
git status

# Stage specific modified files (avoid git add .)
git add units/unit_01_foundations/

# Commit with a clear, imperative message
git commit -m "feat(unit01): add k-mer encoding exercise"

# Strip notebook output metadata automatically
pre-commit run --all-files
```

### 3. Recommended VS Code Extensions for Bioinformatics
To optimize your development environment in Visual Studio Code, install the following extensions:
* **Python** (`ms-python.python`): Python language support, linting, and debugging.
* **Jupyter** (`ms-toolsai.jupyter`): Interactive notebook execution within VS Code.
* **Even Better TOML** / **YAML**: Clean syntax highlighting for environment and workflow files.
* **Markdown All in One** (`yzhang.markdown-all-in-one`): Markdown preview and mathematical formula rendering ($LaTeX$).
