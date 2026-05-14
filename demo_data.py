"""
Generates synthetic DESeq2-like results and sample sheet for demonstration
when real pipeline output is not yet available.
"""

import numpy as np
import pandas as pd

GENE_NAMES = [
    "TP53", "MYC", "BRCA1", "EGFR", "KRAS", "PTEN", "RB1", "VHL",
    "APC", "BRAF", "CDH1", "CDKN2A", "FGFR3", "HRAS", "IDH1", "JAK2",
    "KIT", "MAP2K1", "MET", "MLH1", "MSH2", "NRAS", "PDGFRA", "PIK3CA",
    "RAF1", "RET", "SMAD4", "SMO", "STK11", "TERT", "TSC1", "TSC2",
    "CTNNB1", "FBXW7", "GATA3", "KDM6A", "NF1", "NF2", "NOTCH1", "RUNX1",
    "SF3B1", "SETD2", "SOX2", "SPEN", "TBX3", "TET2", "U2AF1", "ZBTB7A",
    "ATM", "ARID1A", "BAP1", "CEBPA", "CHEK2", "CREBBP", "DNMT3A", "EZH2",
    "FLT3", "FOXA1", "FOXO1", "GATA2", "GPC3", "H3F3A", "HIST1H3B",
    "IGF1R", "KDM5C", "KMT2A", "KMT2C", "KMT2D", "MAP3K1", "MDM2",
    "NCOR1", "NFE2L2", "NTRK1", "PAX5", "PDCD1", "PHOX2B", "PPM1D",
    "PTPN11", "RAC1", "RECQL4", "RIT1", "ROS1", "RRAS", "RUNX1T1",
    "SDHA", "SDHB", "SDHC", "SDHD", "SLC7A8", "SRC", "STAT3", "SUFU",
    "TGFBR1", "TGFBR2", "TNFRSF14", "TRRAP", "WT1", "XPC", "ZEB1", "ZNF217",
]

# Expand with random gene names to fill 500+
EXTRA_GENES = [f"GENE{i:04d}" for i in range(1, 600)]
ALL_GENES = GENE_NAMES + EXTRA_GENES


def generate_deseq2_results(n_genes: int = 500, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    genes = ALL_GENES[:n_genes]

    log2fc = rng.normal(0, 1.5, n_genes)
    # Make ~15% significantly DE
    sig_idx = rng.choice(n_genes, size=int(n_genes * 0.15), replace=False)
    log2fc[sig_idx] += rng.choice([-1, 1], size=len(sig_idx)) * rng.uniform(2, 4, len(sig_idx))

    base_mean = np.exp(rng.normal(5, 2, n_genes))
    stat = log2fc / rng.uniform(0.3, 1.5, n_genes)
    pvalue = 2 * (1 - 0.5 * (1 + np.vectorize(lambda x: np.tanh(abs(x) * 0.8))(stat)))
    pvalue = np.clip(pvalue, 1e-20, 1.0)

    # BH correction (approximate)
    sorted_idx = np.argsort(pvalue)
    padj = pvalue.copy()
    m = n_genes
    for rank, idx in enumerate(sorted_idx):
        padj[idx] = min(1.0, pvalue[idx] * m / (rank + 1))

    df = pd.DataFrame(
        {
            "gene_id": genes,
            "baseMean": np.round(base_mean, 2),
            "log2FoldChange": np.round(log2fc, 4),
            "lfcSE": np.round(rng.uniform(0.1, 0.8, n_genes), 4),
            "stat": np.round(stat, 4),
            "pvalue": np.round(pvalue, 8),
            "padj": np.round(padj, 8),
        }
    )
    return df.sort_values("padj").reset_index(drop=True)


def generate_sample_sheet_template(pipeline: str = "rnaseq") -> pd.DataFrame:
    if pipeline == "rnaseq":
        return pd.DataFrame(
            {
                "sample": ["ctrl_rep1", "ctrl_rep2", "ctrl_rep3", "treat_rep1", "treat_rep2", "treat_rep3"],
                "fastq_1": [
                    "ctrl_rep1_R1.fastq.gz",
                    "ctrl_rep2_R1.fastq.gz",
                    "ctrl_rep3_R1.fastq.gz",
                    "treat_rep1_R1.fastq.gz",
                    "treat_rep2_R1.fastq.gz",
                    "treat_rep3_R1.fastq.gz",
                ],
                "fastq_2": [
                    "ctrl_rep1_R2.fastq.gz",
                    "ctrl_rep2_R2.fastq.gz",
                    "ctrl_rep3_R2.fastq.gz",
                    "treat_rep1_R2.fastq.gz",
                    "treat_rep2_R2.fastq.gz",
                    "treat_rep3_R2.fastq.gz",
                ],
                "strandedness": ["auto"] * 6,
                "condition": ["control", "control", "control", "treated", "treated", "treated"],
            }
        )
    elif pipeline in ("sarek", "exome"):
        return pd.DataFrame(
            {
                "patient": ["patient1", "patient1", "patient2", "patient2"],
                "sex": ["XX", "XX", "XY", "XY"],
                "status": [0, 1, 0, 1],
                "sample": ["normal1", "tumor1", "normal2", "tumor2"],
                "fastq_1": ["normal1_R1.fastq.gz", "tumor1_R1.fastq.gz", "normal2_R1.fastq.gz", "tumor2_R1.fastq.gz"],
                "fastq_2": ["normal1_R2.fastq.gz", "tumor1_R2.fastq.gz", "normal2_R2.fastq.gz", "tumor2_R2.fastq.gz"],
            }
        )
    elif pipeline == "chipseq":
        return pd.DataFrame(
            {
                "sample": ["IP_rep1", "IP_rep2", "input_rep1", "input_rep2"],
                "fastq_1": ["IP_rep1_R1.fastq.gz", "IP_rep2_R1.fastq.gz", "input_rep1_R1.fastq.gz", "input_rep2_R1.fastq.gz"],
                "fastq_2": ["IP_rep1_R2.fastq.gz", "IP_rep2_R2.fastq.gz", "input_rep1_R2.fastq.gz", "input_rep2_R2.fastq.gz"],
                "antibody": ["H3K27me3", "H3K27me3", "", ""],
                "control": ["", "", "input_rep1", "input_rep2"],
            }
        )
    else:
        return pd.DataFrame({"sample": [], "fastq_1": [], "fastq_2": []})


def generate_pca_data(n_samples: int = 6, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    labels = ["control"] * 3 + ["treated"] * 3
    pc1 = [rng.normal(-5, 1) if l == "control" else rng.normal(5, 1) for l in labels]
    pc2 = [rng.normal(0, 2) for _ in labels]
    variance_explained = [38.4, 18.2]
    return pd.DataFrame({"sample": [f"{l}_rep{i+1}" for i, l in enumerate(labels)], "PC1": pc1, "PC2": pc2, "condition": labels}), variance_explained


def generate_multiqc_summary() -> pd.DataFrame:
    samples = ["ctrl_rep1", "ctrl_rep2", "ctrl_rep3", "treat_rep1", "treat_rep2", "treat_rep3"]
    import numpy as np
    rng = np.random.default_rng(0)
    return pd.DataFrame({
        "sample": samples,
        "total_reads": (rng.uniform(20, 40, 6) * 1e6).astype(int),
        "pct_aligned": np.round(rng.uniform(85, 98, 6), 1),
        "pct_duplicates": np.round(rng.uniform(5, 25, 6), 1),
        "median_insert_size": rng.integers(150, 300, 6),
        "pct_gc": np.round(rng.uniform(48, 55, 6), 1),
    })
