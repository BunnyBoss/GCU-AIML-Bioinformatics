#!/usr/bin/env bash
# ==============================================================================
# download_data.sh — Download TCGA-BRCA files directly from cBioPortal GitHub
# ==============================================================================
# Source: https://github.com/cBioPortal/datahub/tree/master/public/brca_tcga_pan_can_atlas_2018
# ==============================================================================

set -e

RAW_DIR="datasets/raw"
mkdir -p "$RAW_DIR"

BASE_URL="https://github.com/cBioPortal/datahub/raw/master/public/brca_tcga_pan_can_atlas_2018"

echo "[*] Downloading raw files from cBioPortal GitHub..."
curl -L -o "$RAW_DIR/data_clinical_patient.txt" "$BASE_URL/data_clinical_patient.txt"
curl -L -o "$RAW_DIR/data_clinical_sample.txt"  "$BASE_URL/data_clinical_sample.txt"
curl -L -o "$RAW_DIR/data_mrna_seq_v2_rsem.txt" "$BASE_URL/data_mrna_seq_v2_rsem.txt"

echo "[✓] Download complete. Files saved in $RAW_DIR/"
