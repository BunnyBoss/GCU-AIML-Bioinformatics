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

You can download course datasets using simple, direct `curl` commands or via the minimal download script [datasets/download_scripts/download_data.sh](download_scripts/download_data.sh):

### 1. TCGA-BRCA PanCancer Atlas Files (cBioPortal GitHub)
* **GitHub Repository:** [`cBioPortal/datahub - brca_tcga_pan_can_atlas_2018`](https://github.com/cBioPortal/datahub/tree/master/public/brca_tcga_pan_can_atlas_2018)
* **Direct Script Execution:**
  ```bash
  # Runs 3 curl commands to fetch clinical patient, clinical sample, and mRNA matrices into datasets/raw/
  bash datasets/download_scripts/download_data.sh
  ```
* **Or Direct `curl` Commands:**
  ```bash
  BASE="https://github.com/cBioPortal/datahub/raw/master/public/brca_tcga_pan_can_atlas_2018"
  curl -L -o datasets/raw/data_clinical_patient.txt "$BASE/data_clinical_patient.txt"
  curl -L -o datasets/raw/data_clinical_sample.txt  "$BASE/data_clinical_sample.txt"
  curl -L -o datasets/raw/data_mrna_seq_v2_rsem.txt "$BASE/data_mrna_seq_v2_rsem.txt"
  ```

### 2. Curated Benchmark Cohort for Lab Exercise 01
* **Location:** [labs/lab_01_binary_classification_pipeline/data/tcga_brca_expression.csv](../labs/lab_01_binary_classification_pipeline/data/tcga_brca_expression.csv)
* **Dimensions:** 670 patient biopsies $\times$ 60 PAM50 and oncogenic driver genes (336 KB). Ready-to-use for immediate modeling without multi-gigabyte raw processing.

### 3. NCBI GEO Microarray Series Matrix (GSE2034 Breast Cancer)
* **Direct NCBI GEO FTP URL:** `https://ftp.ncbi.nlm.nih.gov/geo/series/GSE2nnn/GSE2034/matrix/GSE2034_series_matrix.txt.gz`
* **Direct `wget` Command:**
  ```bash
  wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE2nnn/GSE2034/matrix/GSE2034_series_matrix.txt.gz -P datasets/raw/
  ```
