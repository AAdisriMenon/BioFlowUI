"""
nf-core API wrapper — fetches pipeline metadata, versions, and parameter schemas.
Falls back to a hardcoded catalogue if the network is unavailable.
"""

import requests
import json
from typing import Optional

NFCORE_API = "https://nf-co.re"

PIPELINE_CATALOGUE = {
    "rnaseq": {
        "name": "rnaseq",
        "full_name": "nf-core/rnaseq",
        "description": "RNA sequencing analysis pipeline for quantification of gene/isoform expression",
        "version": "3.14.0",
        "topics": ["rna-seq", "differential-expression", "transcriptomics"],
        "steps": ["FastQC", "Trim Galore", "STAR / Salmon", "featureCounts", "DESeq2", "MultiQC"],
        "runtime_estimate": "2–6 hours",
        "min_cores": 4,
        "min_ram_gb": 32,
        "params": {
            "genome": {
                "label": "Reference genome",
                "type": "select",
                "options": ["GRCh38", "GRCh37", "GRCm39", "GRCm38"],
                "default": "GRCh38",
                "help": "Choose the reference genome matching your organism",
            },
            "aligner": {
                "label": "Aligner",
                "type": "select",
                "options": ["star_salmon", "star_rsem", "hisat2"],
                "default": "star_salmon",
                "help": "STAR+Salmon is recommended for most experiments",
            },
            "deseq2_vst": {
                "label": "Use VST normalisation (DESeq2)",
                "type": "boolean",
                "default": True,
                "help": "Variance-stabilising transformation for downstream PCA/heatmaps",
            },
            "skip_trimming": {
                "label": "Skip adapter trimming",
                "type": "boolean",
                "default": False,
                "help": "Skip Trim Galore (only for pre-trimmed libraries)",
            },
            "min_mapped_reads": {
                "label": "Min mapped reads per sample",
                "type": "integer",
                "default": 5000000,
                "help": "Samples below this threshold are flagged",
            },
        },
    },
    "sarek": {
        "name": "sarek",
        "full_name": "nf-core/sarek",
        "description": "Variant calling pipeline for whole-genome or targeted sequencing",
        "version": "3.4.0",
        "topics": ["wes", "wgs", "variant-calling", "snp", "indel"],
        "steps": ["FastQC", "Trim Galore", "BWA-MEM2", "GATK4", "DeepVariant", "VEP annotation", "MultiQC"],
        "runtime_estimate": "4–12 hours",
        "min_cores": 8,
        "min_ram_gb": 64,
        "params": {
            "genome": {
                "label": "Reference genome",
                "type": "select",
                "options": ["GRCh38", "GRCh37"],
                "default": "GRCh38",
                "help": "Human reference genome build",
            },
            "tools": {
                "label": "Variant callers",
                "type": "multiselect",
                "options": ["haplotypecaller", "deepvariant", "mutect2", "strelka"],
                "default": ["haplotypecaller"],
                "help": "Select one or more variant calling tools",
            },
            "wes": {
                "label": "Whole exome sequencing (WES) mode",
                "type": "boolean",
                "default": True,
                "help": "Adds interval-based processing for targeted panels",
            },
            "skip_annotation": {
                "label": "Skip VEP annotation",
                "type": "boolean",
                "default": False,
                "help": "Skip VEP variant effect prediction",
            },
        },
    },
    "chipseq": {
        "name": "chipseq",
        "full_name": "nf-core/chipseq",
        "description": "ChIP-seq peak calling and differential binding analysis",
        "version": "2.0.0",
        "topics": ["chip-seq", "peak-calling", "epigenomics"],
        "steps": ["FastQC", "Trim Galore", "BWA", "SAMtools", "MACS2", "DiffBind", "MultiQC"],
        "runtime_estimate": "1–4 hours",
        "min_cores": 4,
        "min_ram_gb": 16,
        "params": {
            "genome": {
                "label": "Reference genome",
                "type": "select",
                "options": ["GRCh38", "GRCh37", "GRCm39", "GRCm38"],
                "default": "GRCh38",
                "help": "Reference genome for alignment",
            },
            "peak_type": {
                "label": "Peak type",
                "type": "select",
                "options": ["narrow", "broad", "very-broad"],
                "default": "narrow",
                "help": "Narrow = transcription factors, broad = histone marks",
            },
        },
    },
    "atacseq": {
        "name": "atacseq",
        "full_name": "nf-core/atacseq",
        "description": "ATAC-seq chromatin accessibility analysis pipeline",
        "version": "2.1.2",
        "topics": ["atac-seq", "chromatin-accessibility", "epigenomics"],
        "steps": ["FastQC", "Trim Galore", "BWA", "SAMtools", "MACS2", "deepTools", "MultiQC"],
        "runtime_estimate": "1–3 hours",
        "min_cores": 4,
        "min_ram_gb": 16,
        "params": {
            "genome": {
                "label": "Reference genome",
                "type": "select",
                "options": ["GRCh38", "GRCh37", "GRCm39", "GRCm38"],
                "default": "GRCh38",
                "help": "Reference genome for alignment",
            },
            "macs_gsize": {
                "label": "MACS2 genome size",
                "type": "select",
                "options": ["hs", "mm", "ce", "dm"],
                "default": "hs",
                "help": "Effective genome size for MACS2 peak calling",
            },
        },
    },
}


def get_all_pipelines() -> dict:
    """Try to fetch live pipeline list; fall back to catalogue."""
    try:
        r = requests.get(f"{NFCORE_API}/pipelines.json", timeout=5)
        if r.status_code == 200:
            data = r.json()
            # Merge live data with our detailed catalogue
            live = {p["name"]: p for p in data.get("remote_workflows", [])}
            for key in PIPELINE_CATALOGUE:
                if key in live:
                    PIPELINE_CATALOGUE[key]["version"] = live[key].get(
                        "releases", [{}]
                    )[0].get("tag_name", PIPELINE_CATALOGUE[key]["version"])
    except Exception:
        pass
    return PIPELINE_CATALOGUE


def get_pipeline(name: str) -> Optional[dict]:
    return PIPELINE_CATALOGUE.get(name)


def get_nftest_command(pipeline: str, profile: str = "docker") -> str:
    return f"nextflow run nf-core/{pipeline} -profile test,{profile} --outdir ./test_results"
