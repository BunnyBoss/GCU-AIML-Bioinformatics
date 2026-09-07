# Datasets Repository & Data Management Guide

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  

---

## Overview

High-throughput bioinformatics workflows depend on clean, well-annotated biological datasets spanning multiple molecular modalities:
* **Microarray & RNA-seq expression matrices** (continuous gene counts)
* **DNA methylation beta-value arrays** (epigenetic marks)
* **Genomic DNA & Protein FASTA sequences** (nucleotide/amino acid sequences)
* **Histopathological Whole-Slide Images (WSI)** (biomedical image tiles)
* **Clinical cohort phenotypes & survival tables** (categorical & censored clinical metadata)

This directory provides standardized download scripts, schema definitions, and biological feature dictionaries for all laboratory practicals.

---

## Directory Organization

```
datasets/
├── README.md              # This documentation and data hygiene guide
├── download_scripts/      # Automated Python & Bash fetch scripts with checksum verification
│   └── fetch_datasets.py  # Master download utility
└── raw/                   # Destination folder for raw data files (.gitignored)
```

> ⚠️ **Important Data Hygiene Rule:**  
> The `datasets/raw/` folder is explicitly listed in [.gitignore](../.gitignore). **Never commit raw biological data files (`.csv`, `.tsv`, `.fasta`, `.h5`, `.npy`, `.png`, `.tif`) to Git.** Large biological datasets must be downloaded locally using the provided automation scripts.

---

## Standard Benchmark Datasets Used in Course

| Identifier | Modality | Dimensions / Size | Primary Course Use | Source / Reference |
|---|---|---|---|---|
| **WDBC** | Clinical & Nuclear Imaging | 569 samples $\times$ 30 features | Lab 03, Lab 04 | UCI ML Repository / Wisconsin Diagnostic Breast Cancer |
| **Epigenetic Methylation** | Illumina 450k BeadChip | 650 samples $\times$ 500 CpGs | Lab 02 | NCBI GEO (GSE40279 / Hannum Epigenetic Clock) |
| **TCGA-BRCA RNA-seq** | Transcriptomic Counts | 1,095 samples $\times$ 2,000 HVGs | Lab 01, Lab 05, Lab 10 | The Cancer Genome Atlas (TCGA) via GDC Portal |
| **Promoter DNA Sequences** | Genomic Sequence (FASTA) | 5,000 sequences $\times$ 200 bp | Lab 08 | Eukaryotic Promoter Database (EPD) / JASPAR |
| **Breast Histopathology** | Microscopic Imaging (H&E) | 10,000 image patches ($50\times50$ px) | Lab 07 | Kaggle / Janowczyk et al. Histopathology Benchmark |
| **Serum Proteomics** | Mass Spectrometry Peaks | 216 samples $\times$ 100 m/z features | Lab 06 | FDA-NCI Clinical Proteomics Program |

---

## Downloading Datasets Locally

To automatically fetch and verify all required course datasets into `datasets/raw/`, run:

```bash
# Ensure your environment is active
conda activate gcu-aiml-bioinfo

# Execute the automated fetch script
python datasets/download_scripts/fetch_datasets.py
```

The script performs the following:
1. Downloads compressed archives from institutional GCU mirrors or canonical public repositories (NCBI GEO, UCI, GDC).
2. Computes SHA256 checksums to verify file integrity.
3. Unpacks files into `datasets/raw/<dataset_name>/`.
