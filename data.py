"""
Pipeline catalogue and synthetic demo data.
No real FASTQ files or internet connection needed to explore the app.
"""

import numpy as np
import pandas as pd

# ── Pipeline catalogue ─────────────────────────────────────────────────────────
PIPELINES = {
    "rnaseq": {
        "id": "rnaseq",
        "title": "RNA Sequencing (RNA-seq)",
        "icon": "🧬",
        "tagline": "Compare gene activity between your groups",
        "what_it_does": (
            "Measures which genes are switched ON or OFF in your samples. "
            "Perfect if you want to understand how a disease, drug, or treatment "
            "changes gene expression."
        ),
        "best_for": ["Comparing treated vs untreated cells", "Disease vs healthy tissue", "Drug response studies"],
        "output": ["List of upregulated and downregulated genes", "Interactive volcano plot", "Pathway analysis (KEGG, Reactome, GO)"],
        "nfcore": "nf-core/rnaseq",
        "version": "3.14.0",
        "time": "2 – 6 hours",
        "ram": "32 GB",
    },
    "exome": {
        "id": "exome",
        "title": "Whole Exome Sequencing (WES)",
        "icon": "🔬",
        "tagline": "Find disease-causing mutations in DNA",
        "what_it_does": (
            "Identifies mutations, deletions, and insertions in the protein-coding "
            "regions of the genome. Widely used for rare disease diagnosis and cancer."
        ),
        "best_for": ["Finding inherited disease mutations", "Tumour vs normal comparison", "Rare disease research"],
        "output": ["List of variants (SNPs and indels)", "Variant annotation with clinical databases", "Quality report"],
        "nfcore": "nf-core/sarek",
        "version": "3.4.0",
        "time": "4 – 12 hours",
        "ram": "64 GB",
    },
    "chipseq": {
        "id": "chipseq",
        "title": "ChIP Sequencing (ChIP-seq)",
        "icon": "🧲",
        "tagline": "Discover where proteins bind on DNA",
        "what_it_does": (
            "Maps the locations in the genome where a specific protein "
            "(like a transcription factor or histone mark) is binding. "
            "Useful for understanding gene regulation."
        ),
        "best_for": ["Transcription factor binding sites", "Histone modification profiling", "Epigenetic research"],
        "output": ["Peak locations on genome", "Binding site annotation", "Differential binding analysis"],
        "nfcore": "nf-core/chipseq",
        "version": "2.0.0",
        "time": "1 – 4 hours",
        "ram": "16 GB",
    },
    "atacseq": {
        "id": "atacseq",
        "title": "ATAC Sequencing (ATAC-seq)",
        "icon": "🌊",
        "tagline": "Map open (accessible) regions of DNA",
        "what_it_does": (
            "Identifies regions of chromatin that are 'open' and accessible, "
            "indicating active regulatory elements. "
            "Helps understand which parts of the genome are active in your cells."
        ),
        "best_for": ["Open chromatin profiling", "Regulatory element discovery", "Cell type characterisation"],
        "output": ["Open chromatin peaks", "Motif enrichment", "Quality metrics"],
        "nfcore": "nf-core/atacseq",
        "version": "2.1.2",
        "time": "1 – 3 hours",
        "ram": "16 GB",
    },
}

GENOMES = {
    "Human (Homo sapiens) — hg38 / GRCh38": "GRCh38",
    "Human (Homo sapiens) — hg19 / GRCh37": "GRCh37",
    "Mouse (Mus musculus) — mm39 / GRCm39": "GRCm39",
    "Mouse (Mus musculus) — mm10 / GRCm38": "GRCm38",
    "Rat (Rattus norvegicus)": "Rnor_6.0",
    "Zebrafish (Danio rerio)": "GRCz11",
    "Drosophila (D. melanogaster)": "BDGP6",
    "C. elegans": "WBcel235",
    "Yeast (S. cerevisiae)": "R64-1-1",
}

GENE_SYMBOLS = [
    "TP53","MYC","BRCA1","EGFR","KRAS","PTEN","RB1","VHL","APC","BRAF",
    "CDH1","CDKN2A","FGFR3","HRAS","IDH1","JAK2","KIT","MET","MLH1","MSH2",
    "NRAS","PIK3CA","RET","SMAD4","SMO","STK11","TERT","TSC1","TSC2","CTNNB1",
    "FBXW7","GATA3","KDM6A","NF1","NF2","NOTCH1","RUNX1","SF3B1","SETD2","SOX2",
    "TET2","ATM","ARID1A","BAP1","CEBPA","CHEK2","CREBBP","DNMT3A","EZH2","FLT3",
    "FOXA1","FOXO1","GATA2","IGF1R","KMT2A","KMT2C","KMT2D","MAP3K1","MDM2",
    "NCOR1","NFE2L2","NTRK1","PAX5","PDCD1","PPM1D","PTPN11","RAC1","RIT1",
    "ROS1","RRAS","SDHA","SDHB","SDHC","SDHD","SRC","STAT3","SUFU","TGFBR1",
    "TGFBR2","TNFRSF14","WT1","ZEB1","ZNF217","BCL2","CCND1","CDK4","CDK6",
    "FGFR1","FGFR2","HMGA2","LMO2","MYCN","PDGFRA","RAF1","RHOA","RICTOR",
] + [f"GENE{i:04d}" for i in range(1, 500)]


def generate_deseq2_results(n: int = 500, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    genes = GENE_SYMBOLS[:n]
    lfc = rng.normal(0, 1.2, n)
    sig = rng.choice(n, size=int(n * 0.14), replace=False)
    lfc[sig] += rng.choice([-1, 1], len(sig)) * rng.uniform(1.8, 4.5, len(sig))
    base_mean = np.exp(rng.normal(5, 2, n))
    pval = np.clip(2 * (1 - 0.5 * (1 + np.tanh(np.abs(lfc / rng.uniform(0.4, 1.2, n))))), 1e-20, 1.0)
    order = np.argsort(pval)
    padj = pval.copy()
    for rank, idx in enumerate(order):
        padj[idx] = min(1.0, pval[idx] * n / (rank + 1))
    return pd.DataFrame({
        "Gene": genes,
        "Mean Expression": np.round(base_mean, 1),
        "Log2 Fold Change": np.round(lfc, 3),
        "p-value": np.round(pval, 8),
        "Adjusted p-value": np.round(padj, 8),
    }).sort_values("Adjusted p-value").reset_index(drop=True)


def generate_pca(seed: int = 42):
    rng = np.random.default_rng(seed)
    labels = ["Control"] * 3 + ["Treated"] * 3
    pc1 = [rng.normal(-6, 0.8) if l == "Control" else rng.normal(6, 0.8) for l in labels]
    pc2 = [rng.normal(0, 2) for _ in labels]
    return pd.DataFrame({
        "Sample": [f"{l} rep{i+1}" for i, l in enumerate(labels)],
        "PC1": pc1, "PC2": pc2, "Group": labels,
    }), [41.3, 17.8]


def generate_qc(seed: int = 42):
    rng = np.random.default_rng(seed)
    samples = ["Control_rep1", "Control_rep2", "Control_rep3", "Treated_rep1", "Treated_rep2", "Treated_rep3"]
    return pd.DataFrame({
        "Sample": samples,
        "Total Reads": (rng.uniform(22, 38, 6) * 1e6).astype(int),
        "% Aligned": np.round(rng.uniform(88, 97, 6), 1),
        "% Duplicates": np.round(rng.uniform(8, 22, 6), 1),
        "% GC": np.round(rng.uniform(49, 54, 6), 1),
        "Status": ["✅ Pass"] * 5 + ["✅ Pass"],
    })


def sample_sheet_template(pipeline: str) -> pd.DataFrame:
    if pipeline == "rnaseq":
        return pd.DataFrame({
            "sample_name": ["Control_rep1", "Control_rep2", "Control_rep3",
                            "Treated_rep1", "Treated_rep2", "Treated_rep3"],
            "fastq_read1_path": [
                "/path/to/ctrl1_R1.fastq.gz", "/path/to/ctrl2_R1.fastq.gz",
                "/path/to/ctrl3_R1.fastq.gz", "/path/to/treat1_R1.fastq.gz",
                "/path/to/treat2_R1.fastq.gz", "/path/to/treat3_R1.fastq.gz",
            ],
            "fastq_read2_path": [
                "/path/to/ctrl1_R2.fastq.gz", "/path/to/ctrl2_R2.fastq.gz",
                "/path/to/ctrl3_R2.fastq.gz", "/path/to/treat1_R2.fastq.gz",
                "/path/to/treat2_R2.fastq.gz", "/path/to/treat3_R2.fastq.gz",
            ],
            "group": ["control", "control", "control", "treated", "treated", "treated"],
        })
    elif pipeline == "exome":
        return pd.DataFrame({
            "patient_id": ["Patient_01", "Patient_01", "Patient_02", "Patient_02"],
            "sample_name": ["Normal_01", "Tumour_01", "Normal_02", "Tumour_02"],
            "sample_type": ["normal", "tumour", "normal", "tumour"],
            "fastq_read1_path": [
                "/path/to/norm1_R1.fastq.gz", "/path/to/tum1_R1.fastq.gz",
                "/path/to/norm2_R1.fastq.gz", "/path/to/tum2_R1.fastq.gz",
            ],
            "fastq_read2_path": [
                "/path/to/norm1_R2.fastq.gz", "/path/to/tum1_R2.fastq.gz",
                "/path/to/norm2_R2.fastq.gz", "/path/to/tum2_R2.fastq.gz",
            ],
        })
    else:
        return pd.DataFrame({
            "sample_name": ["IP_rep1", "IP_rep2", "Input_rep1", "Input_rep2"],
            "fastq_read1_path": [
                "/path/to/ip1_R1.fastq.gz", "/path/to/ip2_R1.fastq.gz",
                "/path/to/in1_R1.fastq.gz", "/path/to/in2_R1.fastq.gz",
            ],
            "fastq_read2_path": [
                "/path/to/ip1_R2.fastq.gz", "/path/to/ip2_R2.fastq.gz",
                "/path/to/in1_R2.fastq.gz", "/path/to/in2_R2.fastq.gz",
            ],
            "antibody_or_control": ["H3K27me3", "H3K27me3", "Input", "Input"],
        })


PATHWAY_DEMO = [
    {"Pathway": "Cell Cycle Regulation", "Database": "KEGG", "Score": 2.41, "FDR": 0.0001, "Direction": "⬆ Up"},
    {"Pathway": "DNA Replication", "Database": "KEGG", "Score": 2.18, "FDR": 0.0003, "Direction": "⬆ Up"},
    {"Pathway": "Ribosome Biogenesis", "Database": "Reactome", "Score": 1.85, "FDR": 0.0011, "Direction": "⬆ Up"},
    {"Pathway": "mRNA Splicing", "Database": "Reactome", "Score": 1.72, "FDR": 0.0024, "Direction": "⬆ Up"},
    {"Pathway": "Oxidative Phosphorylation", "Database": "KEGG", "Score": 1.61, "FDR": 0.0038, "Direction": "⬆ Up"},
    {"Pathway": "p53 Signalling", "Database": "KEGG", "Score": -1.98, "FDR": 0.0005, "Direction": "⬇ Down"},
    {"Pathway": "Apoptosis", "Database": "KEGG", "Score": -1.76, "FDR": 0.0009, "Direction": "⬇ Down"},
    {"Pathway": "DNA Damage Response", "Database": "Reactome", "Score": -1.63, "FDR": 0.0021, "Direction": "⬇ Down"},
    {"Pathway": "Immune Response", "Database": "GO:BP", "Score": -1.55, "FDR": 0.0044, "Direction": "⬇ Down"},
    {"Pathway": "TGF-β Signalling", "Database": "KEGG", "Score": -1.48, "FDR": 0.0077, "Direction": "⬇ Down"},
    {"Pathway": "Wnt Signalling", "Database": "KEGG", "Score": 1.44, "FDR": 0.0093, "Direction": "⬆ Up"},
    {"Pathway": "PI3K-Akt Pathway", "Database": "KEGG", "Score": 1.38, "FDR": 0.0131, "Direction": "⬆ Up"},
]
