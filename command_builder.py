"""
Builds the Nextflow CLI command string from session_state variables.
"""

import streamlit as st


def build_nextflow_command() -> str:
    s = st.session_state
    pipeline = s.get("pipeline", "rnaseq")
    genome = s.get("genome", "GRCh38")
    profile = s.get("profile", "docker")
    outdir = s.get("outdir", "./results")
    resume = s.get("resume", True)

    lines = [f"nextflow run nf-core/{pipeline} \\"]
    lines.append(f"  --input samplesheet.csv \\")
    lines.append(f"  --outdir {outdir} \\")
    lines.append(f"  --genome {genome} \\")

    # Pipeline-specific params
    if pipeline == "rnaseq":
        aligner = s.get("aligner", "star_salmon")
        lines.append(f"  --aligner {aligner} \\")
        if s.get("deseq2_vst", True):
            lines.append(f"  --deseq2_vst \\")
        if s.get("skip_trimming", False):
            lines.append(f"  --skip_trimming \\")
        min_reads = s.get("min_mapped_reads", 5000000)
        if min_reads != 5000000:
            lines.append(f"  --min_mapped_reads {min_reads} \\")

    elif pipeline == "sarek":
        tools = s.get("tools", ["haplotypecaller"])
        if tools:
            lines.append(f"  --tools {','.join(tools)} \\")
        if s.get("wes", True):
            lines.append(f"  --wes \\")
        if s.get("skip_annotation", False):
            lines.append(f"  --skip_annotation \\")

    elif pipeline == "chipseq":
        peak_type = s.get("peak_type", "narrow")
        lines.append(f"  --peak_type {peak_type} \\")

    elif pipeline == "atacseq":
        macs_gsize = s.get("macs_gsize", "hs")
        lines.append(f"  --macs_gsize {macs_gsize} \\")

    lines.append(f"  -profile {profile} \\")

    # Extra modules
    extra_modules = s.get("extra_modules", [])
    for mod in extra_modules:
        lines.append(f"  --{mod} \\")

    if resume:
        lines.append(f"  -resume")
    else:
        # remove trailing backslash from last real line
        pass

    # Clean up trailing backslash on last line
    if lines[-1].endswith(" \\"):
        lines[-1] = lines[-1][:-2]

    return "\n".join(lines)


def build_docker_pull_commands(pipeline: str) -> list[str]:
    """Returns docker pull commands for key containers."""
    containers = {
        "rnaseq": [
            "docker pull nfcore/rnaseq:3.14.0",
            "docker pull quay.io/biocontainers/star:2.7.10b--h9ee0642_0",
            "docker pull quay.io/biocontainers/salmon:1.10.2--hecfa306_0",
            "docker pull quay.io/biocontainers/fastqc:0.12.1--hdfd78af_0",
        ],
        "sarek": [
            "docker pull nfcore/sarek:3.4.0",
            "docker pull broadinstitute/gatk:4.4.0.0",
            "docker pull quay.io/biocontainers/bwa-mem2:2.2.1--hd03093a_2",
        ],
        "chipseq": [
            "docker pull nfcore/chipseq:2.0.0",
            "docker pull quay.io/biocontainers/macs2:2.2.9.1--py39hf95cd2a_0",
        ],
        "atacseq": [
            "docker pull nfcore/atacseq:2.1.2",
            "docker pull quay.io/biocontainers/macs2:2.2.9.1--py39hf95cd2a_0",
        ],
    }
    return containers.get(pipeline, [])


def build_singularity_command(pipeline: str, version: str) -> str:
    return f"singularity pull docker://nfcore/{pipeline}:{version}"


def get_nextflow_install_instructions() -> str:
    return """# Install Nextflow
curl -s https://get.nextflow.io | bash
sudo mv nextflow /usr/local/bin/

# Verify
nextflow -version

# Install nf-core tools (optional but recommended)
pip install nf-core"""
