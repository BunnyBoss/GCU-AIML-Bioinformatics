#!/usr/bin/env python3
"""
download_lab_02_regression_data.py
===================================
Fetches the unscaled, raw physiological diabetes cohort from Scikit-Learn,
constructs a realistic patient cohort table, injects controlled real-world
data quality anomalies (duplicates, missing values, non-fitting outliers),
and exports the raw file to datasets/raw/lab_02_day_19_diabetes_regression_raw.csv.

Curriculum: GCU M.Sc. Bioinformatics — Course 02BMSBI24365
Session: Lab Exercise 02 (Day 19 / Week 10)
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

# Set reproducible seed for data artifact consistency
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# Resolve project paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "datasets" / "raw"
OUTPUT_FILE = OUTPUT_DIR / "lab_02_day_19_diabetes_regression_raw.csv"

def fetch_and_inject_anomalies() -> pd.DataFrame:
    print("[*] Fetching raw, non-standardized diabetes cohort from Scikit-Learn...")
    # scaled=False ensures features are natural biological units (years, kg/m², mmHg, mg/dL)
    bunch = load_diabetes(scaled=False, as_frame=True)
    df = bunch.data.copy()
    df["target"] = bunch.target.values

    # Rename lipid/serum markers for biological clarity
    column_mapping = {
        "s1": "s1_tc",      # Total Cholesterol (mg/dL)
        "s2": "s2_ldl",     # Low-Density Lipoproteins (mg/dL)
        "s3": "s3_hdl",     # High-Density Lipoproteins (mg/dL)
        "s4": "s4_tch",     # Total Cholesterol / HDL ratio
        "s5": "s5_ltg",     # Log of serum triglycerides
        "s6": "s6_glu"      # Fasting Blood Glucose (mg/dL)
    }
    df.rename(columns=column_mapping, inplace=True)

    # Prepend structured patient identifiers
    n_samples = len(df)
    patient_ids = [f"PAT_{i+1:03d}" for i in range(n_samples)]
    df.insert(0, "patient_id", patient_ids)

    print(f"[*] Base cohort loaded: {df.shape[0]} patients, {df.shape[1]} columns.")

    # --------------------------------------------------------------------------
    # 1. Inject Controlled Duplicate Rows (6 patients duplicated)
    # --------------------------------------------------------------------------
    dup_indices = [14, 45, 112, 230, 310, 401]
    duplicate_rows = df.iloc[dup_indices].copy()
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    print(f"[+] Injected {len(dup_indices)} duplicate patient records.")

    # --------------------------------------------------------------------------
    # 2. Inject Controlled Non-Fitting / Corrupted Values
    # --------------------------------------------------------------------------
    # Corrupted age entries (negative / impossible placeholder)
    df.loc[25, "age"] = -99.0
    df.loc[188, "age"] = -45.0

    # Physiologically impossible clinical readings
    df.loc[52, "bmi"] = -5.0       # Negative BMI is physically impossible
    df.loc[340, "bp"] = 0.0        # Zero blood pressure is clinically invalid for a live cohort
    print("[+] Injected 4 non-fitting/corrupted clinical values (negative age, zero BP, negative BMI).")

    # --------------------------------------------------------------------------
    # 3. Inject Controlled Missing Values (~4% missing in select columns)
    # --------------------------------------------------------------------------
    missing_cols = ["bmi", "bp", "s6_glu"]
    n_missing_per_col = int(n_samples * 0.04)  # ~17 missing entries per target column

    for col in missing_cols:
        # Avoid overriding the corrupted rows created above
        eligible_indices = [idx for idx in range(n_samples) if idx not in [25, 52, 188, 340]]
        chosen_indices = np.random.choice(eligible_indices, size=n_missing_per_col, replace=False)
        df.loc[chosen_indices, col] = np.nan
        print(f"[+] Injected {n_missing_per_col} NaN values into '{col}'.")

    return df

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_df = fetch_and_inject_anomalies()

    raw_df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n[✓] Raw dataset successfully exported to:\n    {OUTPUT_FILE}")
    print(f"[*] Total rows: {len(raw_df)} | Total columns: {len(raw_df.columns)}")
    print(f"[*] Total missing values: {raw_df.isnull().sum().sum()}")
    print(f"[*] Duplicate row count: {raw_df.duplicated().sum()}")

if __name__ == "__main__":
    main()
