# 🧬 BioFlow UI — nf-core Pipeline Assistant

A **no-code web application** that lets wet-lab scientists run state-of-the-art
bioinformatics pipelines (RNA-seq, WES, ChIP-seq, ATAC-seq) and explore results
— **no bioinformatics knowledge required**.

---

## ✅ Quick start (3 commands)

```bash
# 1. Clone / enter the project
cd bioflow_ui

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

The browser will open at **http://localhost:8501** automatically.

---

## 📦 Features

| Feature | Description |
|---|---|
| Pipeline selector | Choose RNA-seq, WES, ChIP-seq, or ATAC-seq with plain-English explanations |
| Sample sheet builder | Editable table — no CSV knowledge needed |
| Parameter configuration | Sensible defaults + plain-language tooltips |
| Container setup | Docker / Singularity / Conda — auto-generates Nextflow command |
| Run pipeline | Live log streaming + progress bars |
| Demo mode | Explore all features with synthetic data, no files needed |
| Volcano plot | Interactive, labelled, export-ready |
| PCA plot | Sample clustering visualisation |
| MA plot | Expression vs fold-change |
| MultiQC summary | Alignment QC at a glance |
| Pathway analysis | GSEA + ORA via gseapy (KEGG, Reactome, GO) |
| Download results | DEG table and pathway results as CSV |

---

## 🖥️ System requirements

### For the Streamlit UI (this app)
- Python ≥ 3.10
- 4 GB RAM

### For actually running pipelines
- **Java ≥ 11** (required by Nextflow)
- **Nextflow** — install with: `curl -s https://get.nextflow.io | bash`
- **Docker** (recommended) OR **Singularity** (for HPC) OR **Conda**
- RAM: 32 GB for RNA-seq, 64 GB for WES
- Storage: 100–500 GB per run

---

## 🗂️ Project structure

```
bioflow_ui/
├── app.py                          # Home page + session state init
├── nfcore_api.py                   # nf-core REST API + pipeline catalogue
├── command_builder.py              # Nextflow command generator
├── docker_check.py                 # Environment prerequisite checker
├── demo_data.py                    # Synthetic data for demo mode
├── requirements.txt
├── README.md
└── pages/
    ├── 1_🧬_Pipeline_Selector.py   # Choose pipeline
    ├── 2_📂_Sample_Inputs.py       # Build sample sheet
    ├── 3_⚙️_Configuration.py       # Set parameters
    ├── 4_🐳_Container_Setup.py     # Container + command preview
    ├── 5_▶️_Run_Pipeline.py        # Launch + live logs
    ├── 6_📊_Results.py             # Volcano, PCA, DEG table
    └── 7_🔬_Pathway_Analysis.py    # GSEA, ORA, dot plot
```

---

## 🧪 Demo mode

Toggle **Demo mode** in the sidebar (ON by default). This lets you:
- Navigate every page
- See interactive volcano, PCA, MA plots
- Run pathway analysis
- Download result tables

…all with **synthetic data**, without any real FASTQ files or Nextflow installed.

---

## 🔬 Using with real data

1. Turn demo mode **OFF** in the sidebar
2. Make sure **Nextflow + Docker** are installed (Step 4 checks this)
3. Build your sample sheet with real FASTQ file paths
4. Click **Launch pipeline** on Step 5
5. View results on Steps 6 & 7 once finished

---

## 🧬 Supported nf-core pipelines

| Pipeline | nf-core name | Use case |
|---|---|---|
| RNA-seq | `nf-core/rnaseq` | Differential gene expression |
| WES / WGS | `nf-core/sarek` | Variant calling (SNPs, indels) |
| ChIP-seq | `nf-core/chipseq` | Peak calling, differential binding |
| ATAC-seq | `nf-core/atacseq` | Chromatin accessibility |

---

## 🤝 Community

- [nf-core community](https://nf-co.re)
- [Nextflow documentation](https://www.nextflow.io/docs/latest/)
- [nf-core Slack](https://nf-co.re/join/slack)

---

## 📄 License

MIT — free to use, modify, and distribute.
