#!/usr/bin/env python3
"""
preprocess_raw_tcga.py
======================
Extracts and processes raw TCGA-BRCA PanCancer Atlas files from cBioPortal into
the curated PAM50 Luminal A vs. Basal-like benchmark dataset.

Workflow:
1. Ingest clinical metadata (patient & sample annotations).
2. Filter for Primary tumors of interest:
   - BRCA_LumA  (Luminal A, target = 0)
   - BRCA_Basal (Basal-like / Triple-Negative, target = 1)
3. Ingest raw mRNA-seq RSEM matrix (data_mrna_seq_v2_rsem.txt).
4. Extract 60 curated PAM50 & oncogenic driver genes.
5. Transpose matrix (samples as rows, genes as columns) and save:
   - data/tcga_brca_expression.csv
"""

import os
import sys
import pandas as pd

# 60 Curated PAM50 Signature & Breast Cancer Oncogenic Driver Genes
TARGET_GENES = [
    "ACTR3B", "ANLN", "BAG1", "BCL2", "BIRC5", "BLVRA", "CCNB1", "CCNE1",
    "CDC20", "CDC6", "CDH3", "CENPF", "CEP55", "CXXC5", "EGFR", "ERBB2",
    "ESR1", "EXO1", "FGFR4", "FOXA1", "FOXC1", "GATA3", "GLI3", "GRB7",
    "KIF2C", "KNTC2", "KRT14", "KRT17", "KRT5", "MAPT", "MDM2", "MELK",
    "MIA", "MKI67", "MLPH", "MMP11", "MYBL2", "MYC", "NAT1", "NDC80",
    "NELFE", "NUF2", "ORC6", "PGR", "PHGDH", "PTTG1", "RRM2", "SFRP1",
    "SLC39A6", "TMEM45B", "TYMS", "UBE2C", "UBE2T", "TP53", "PIK3CA",
    "AKT1", "PTEN", "RB1", "CDK4", "CDK6"
]

def locate_paths():
    """Locate raw inputs and target outputs relative to current working directory."""
    candidate_raw_dirs = [
        "datasets/raw",
        "../../datasets/raw",
        "../datasets/raw"
    ]
    raw_dir = None
    for d in candidate_raw_dirs:
        if os.path.exists(os.path.join(d, "data_clinical_patient.txt")):
            raw_dir = d
            break

    if raw_dir is None:
        print("[!] ERROR: Raw cBioPortal files not found in datasets/raw/.")
        print("    Please run the download script first:")
        print("    bash datasets/download_scripts/download_data.sh")
        sys.exit(1)

    # Determine output destination
    candidate_out_dirs = [
        "labs/lab_01_binary_classification_pipeline/data",
        "data"
    ]
    out_dir = candidate_out_dirs[0] if os.path.exists("labs") else candidate_out_dirs[1]
    os.makedirs(out_dir, exist_ok=True)
    out_csv = os.path.join(out_dir, "tcga_brca_expression.csv")

    return raw_dir, out_csv

def main():
    raw_dir, out_csv = locate_paths()
    print(f"[*] Ingesting raw cBioPortal clinical files from: {raw_dir}")

    # 1. Ingest Clinical Patient & Sample annotations
    pat_file = os.path.join(raw_dir, "data_clinical_patient.txt")
    samp_file = os.path.join(raw_dir, "data_clinical_sample.txt")
    mrna_file = os.path.join(raw_dir, "data_mrna_seq_v2_rsem.txt")

    df_pat = pd.read_csv(pat_file, sep="\t", comment="#", low_memory=False)
    df_samp = pd.read_csv(samp_file, sep="\t", comment="#", low_memory=False)

    # 2. Merge clinical metadata & filter primary tumors for LumA vs. Basal
    clinical = pd.merge(
        df_samp[["SAMPLE_ID", "PATIENT_ID", "SAMPLE_TYPE"]],
        df_pat[["PATIENT_ID", "SUBTYPE"]],
        on="PATIENT_ID"
    )
    cohort = clinical[
        (clinical["SAMPLE_TYPE"] == "Primary") &
        (clinical["SUBTYPE"].isin(["BRCA_LumA", "BRCA_Basal"]))
    ].drop_duplicates(subset=["PATIENT_ID"]).sort_values("SAMPLE_ID").reset_index(drop=True)

    cohort["target"] = cohort["SUBTYPE"].map({"BRCA_LumA": 0, "BRCA_Basal": 1})
    print(f"[✓] Clinical filtering complete: {len(cohort)} patients")
    print(cohort["SUBTYPE"].value_counts().to_string())

    # 3. Ingest raw mRNA expression matrix (20,531 genes)
    print(f"\n[*] Slicing raw mRNA expression matrix from: {mrna_file} (147 MB)...")
    mrna = pd.read_csv(mrna_file, sep="\t", index_col=0).drop(columns=["Entrez_Gene_Id"], errors="ignore")

    # Rename gene aliases if needed (e.g., ORC6L -> ORC6)
    mrna.rename(index={"ORC6L": "ORC6"}, inplace=True)

    available_genes = [g for g in TARGET_GENES if g in mrna.index]
    valid_samples = [s for s in cohort["SAMPLE_ID"] if s in mrna.columns]

    print(f"[✓] Matching samples found: {len(valid_samples)} | Signature genes: {len(available_genes)}/60")

    # 4. Slice and transpose (samples as rows, genes as columns)
    expr = mrna.loc[available_genes, valid_samples].T

    # 5. Combine metadata and expression profiles
    df_final = cohort.set_index("SAMPLE_ID").loc[valid_samples, ["PATIENT_ID", "SUBTYPE", "target"]].join(expr)
    df_final.reset_index(names=["sample_id"], inplace=True)
    df_final.rename(columns={"PATIENT_ID": "patient_id", "SUBTYPE": "subtype"}, inplace=True)

    # 6. Save final CSV
    df_final.to_csv(out_csv, index=False)
    print(f"\n[✓] Assembled dataset saved to: {out_csv}")
    print(f"    - Dimensions: {df_final.shape[0]} samples × {df_final.shape[1]} columns")
    print(f"    - Class distribution:\n{df_final['subtype'].value_counts().to_string()}")

if __name__ == "__main__":
    main()
