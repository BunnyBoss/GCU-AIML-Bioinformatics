# Environment & Package Management with Conda: A Crash Course for Bioinformaticians

*A practical, comprehensive reference for managing Python environments, installing bioinformatics tools via Bioconda, and ensuring end-to-end scientific reproducibility.*

---

## 1. Why Isolated Environments are Essential in Bioinformatics & ML

Bioinformatics workflows rely on an intricate web of tools: C-libraries for sequence alignment (e.g., SAMtools, Bowtie2), specialized biological Python packages (e.g., BioPython, PyTDC), and heavy machine learning frameworks (e.g., Scikit-Learn, PyTorch, TensorFlow).

If you install all these packages globally into your default Python installation, you will inevitably hit **"Dependency Hell"**:

```
❌ The Global Installation Disaster:
Project A requires:  scikit-learn==1.3.0  --> requires  numpy==1.24.3
Project B requires:  biopython==1.78     --> requires  numpy==1.19.5
💥 Result: Upgrading NumPy for Project A permanently breaks Project B!
```

### The Solution: Conda Virtual Environments
A Conda environment is a completely isolated directory that contains a specific Python version and an exact set of installed libraries. Switching between projects is as simple as activating a different environment.

---

## 2. The Ecosystem: Conda vs. Pip vs. Mamba vs. Bioconda

| Tool / Concept | What It Is | Best Used For |
|---|---|---|
| **Conda** | Language-agnostic package and environment manager | Managing Python versions, C-libraries, binaries, and virtual environments |
| **Pip** | The official Python Package Installer | Installing pure Python libraries from PyPI when not available on Conda |
| **Mamba** | A high-speed C++ drop-in replacement for Conda | Blazing-fast environment creation and dependency solving |
| **Bioconda** | A dedicated Conda channel with >9,000 bioinformatics packages | Installing tools like SAMtools, BLAST, FastQC, Bedtools, and BioPython |
| **Miniforge** | Minimal installer configured with `conda-forge` as default | The cleanest, lightest distribution for data science & bioinformatics |

---

## 3. Configuring Conda Channels for Bioinformatics (Run Once)

Conda searches for packages across remote repositories called **channels**. To ensure that bioinformatics tools and general data science libraries resolve without conflicts, configure your channel priority order strictly:

```bash
# 1. Configure the channel priority order (highest to lowest)
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge

# 2. Enforce strict channel priority to prevent dependency mixing
conda config --set channel_priority strict

# 3. Verify your configured channels
conda config --show channels
```

> **Why this order matters:** `conda-forge` provides the most up-to-date core Python and C-compilers, while `bioconda` builds domain-specific biological packages on top of `conda-forge`.

---

## 4. Daily Core Workflow: Essential Commands

### Step A: Creating an Environment
```bash
# Create a fresh environment with Python 3.10 named 'bio_ml'
conda create -n bio_ml python=3.10 -y

# Verify the environment was created
conda env list
```

### Step B: Activating & Deactivating Environments
```bash
# Activate your new environment
conda activate bio_ml

# Notice your terminal prompt changes: (base) --> (bio_ml)

# Deactivate and return to base when finished
conda deactivate
```

### Step C: Installing Core Machine Learning & Data Science Packages
```bash
# Always install packages while your target environment is active
conda activate bio_ml

# Install core data science stack from conda-forge
conda install -c conda-forge numpy pandas scikit-learn matplotlib seaborn jupyterlab -y
```

### Step D: Installing Bioinformatics-Specific Tools via Bioconda
```bash
# Install genomics and sequence analysis packages
conda install -c bioconda biopython samtools blast -y
```

### Step E: Inspecting Installed Packages
```bash
# List all packages and exact versions installed in the active environment
conda list

# Search whether a specific package is available on Conda channels
conda search biopython
```

### Step F: Removing Packages or Deleting an Entire Environment
```bash
# Remove a single package from the active environment
conda remove biopython -y

# Delete an entire environment that is no longer needed
conda deactivate
conda env remove -n bio_ml -y
```

---

## 5. Sharing & Reproducibility with `environment.yml`

In computational biology, saving and publishing your environment definition is mandatory for reproducible research.

### Exporting Your Active Environment:
```bash
# Export the environment specification without OS-specific build hashes
conda env export --no-builds > environment.yml
```

### Creating an Environment from an `environment.yml` File:
```bash
# Anyone on Linux, macOS, or Windows can recreate your exact environment with:
conda env create -f environment.yml
```

### Production-Ready `environment.yml` for this Course:
Save this as `environment.yml` in your project root:

```yaml
name: bio_ml
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - python=3.10
  - numpy>=1.24.0
  - pandas>=2.0.0
  - scikit-learn>=1.3.0
  - matplotlib>=3.7.0
  - seaborn>=0.12.0
  - biopython>=1.81
  - ipykernel
  - jupyterlab
  - pip
  - pip:
    # Use pip only for packages not available on Conda
    - torchsummary
```

---

## 6. Connecting Your Conda Environment to Jupyter Notebooks & VS Code

To make your Conda environment appear in Jupyter Lab, Jupyter Notebooks, or VS Code:

```bash
# 1. Activate your environment
conda activate bio_ml

# 2. Install ipykernel
conda install -c conda-forge ipykernel -y

# 3. Register your environment as a selectable Jupyter Kernel
python -m ipykernel install --user --name=bio_ml --display-name "Python (bio_ml)"
```

* **In VS Code:** Open your `.ipynb` notebook $\to$ Click the **Kernel Selector** in the top-right corner $\to$ Select **Python Environments** $\to$ Choose **Python (bio_ml)**.
* **In JupyterLab:** Click **New Notebook** $\to$ Select **Python (bio_ml)** from the dropdown.

---

## 7. Best Practices & Troubleshooting

### Golden Rules:
1. **Never install packages into the `base` environment:** Keep `base` clean; use it only to manage your other environments.
2. **Speed up slow dependency solving with Mamba:**
   ```bash
   # Install mamba into your base environment
   conda install -n base -c conda-forge mamba -y
   
   # Use mamba exactly like conda, but 10x faster:
   mamba create -n bio_ml python=3.10 scikit-learn pandas -y
   ```
3. **Free up disk space periodically:**
   ```bash
   # Remove unused package tarballs and cached index files
   conda clean --all -y
   ```

---

## 8. Summary Command Cheat Sheet

| Command | Action |
|---|---|
| `conda create -n <name> python=3.10 -y` | Create a new isolated environment |
| `conda activate <name>` | Switch into the specified environment |
| `conda deactivate` | Exit the current environment |
| `conda env list` | Display all environments on your system |
| `conda install -c conda-forge <pkg>` | Install a data science package |
| `conda install -c bioconda <pkg>` | Install a bioinformatics tool |
| `conda list` | List all installed packages in current environment |
| `conda env export --no-builds > env.yml` | Save environment recipe for sharing |
| `conda env create -f env.yml` | Build an environment from a YAML file |
| `conda clean --all -y` | Delete package caches to free disk space |

---

## 9. Curated Resources for Further Learning

1. **[Official Conda User Guide & Cheat Sheet (PDF)](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)**  
   *The official quick-reference card summarizing environment creation, cloning, and package queries.*
2. **[Bioconda Documentation & Package Index](https://bioconda.github.io/)**  
   *Search through >9,000 biological software packages and view installation instructions.*
3. **[Software Carpentry: Managing Python Environments with Conda](https://carpentries-incubator.github.io/introduction-to-conda-for-data-science/)**  
   *A researcher-oriented, step-by-step introduction to reproducible data science environments.*
4. **[Miniforge Project Repository](https://github.com/conda-forge/miniforge)**  
   *The community-led, minimal installer that preconfigures `conda-forge` without licensing bloat.*
5. **[Building Reproducible Bioinformatics Workflows with Bioconda](https://bioconda.github.io/user/install.html)**  
   *Best practices for integrating Bioconda into containerized and High-Performance Computing (HPC) environments.*
