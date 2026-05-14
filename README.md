# 🧬 BioFlow — Genomics for Everyone

> **Run professional genomics pipelines without writing a single line of code.**

BioFlow is a web application that lets wet-lab scientists run [nf-core](https://nf-co.re) bioinformatics pipelines and explore results through an easy point-and-click interface.

---

## ✨ What can BioFlow do?

| Analysis | What it's for |
|---|---|
| **RNA-seq** | Find which genes are switched on/off between your samples |
| **Whole Exome Sequencing** | Find disease-causing mutations in DNA |
| **ChIP-seq** | Map where proteins bind on DNA |
| **ATAC-seq** | Find open (active) regions of chromatin |

**Results include:**
- Volcano plots, PCA plots, MA plots
- Differentially expressed gene tables (downloadable)
- Pathway analysis (KEGG, Reactome, GO)
- QC summary report

---

## 🚀 Run locally in 3 steps

### Step 1 — Get the code
```bash
git clone https://github.com/YOUR_USERNAME/bioflow.git
cd bioflow
```

### Step 2 — Install Python packages
```bash
pip install -r requirements.txt
```
> Need Python? Download it from [python.org](https://www.python.org/downloads/) (version 3.10 or newer).

### Step 3 — Start the app
```bash
streamlit run app.py
```
The app will open in your browser at **http://localhost:8501**

---

## ☁️ Deploy on Streamlit Cloud (free, shareable link)

1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → choose your forked repo → set main file to `app.py`
4. Click **Deploy** — your app will be live at a public URL in ~2 minutes

---

## 💻 To actually run pipelines (not demo mode)

BioFlow's demo mode lets you explore all features with synthetic data. To run real analyses on your own FASTQ files, you also need:

| Tool | Purpose | Install |
|---|---|---|
| **Java 11+** | Required by Nextflow | [adoptium.net](https://adoptium.net) |
| **Nextflow** | Pipeline engine | `curl -s https://get.nextflow.io \| bash` |
| **Docker** | Runs the tools in containers | [docker.com](https://docs.docker.com/get-docker/) |

> **HPC cluster users:** Singularity is supported instead of Docker. Ask your IT team.

---

## 📁 Project structure

```
bioflow/
├── app.py                          ← Home page (start here)
├── styles.py                       ← All CSS styling
├── data.py                         ← Pipeline info & demo data
├── requirements.txt                ← Python dependencies
├── .streamlit/
│   └── config.toml                 ← App theme & settings
└── pages/
    ├── 1_🧬_Choose_Analysis.py     ← Pick RNA-seq / WES / etc.
    ├── 2_📂_Your_Samples.py        ← Enter sample names & files
    ├── 3_⚙️_Settings.py            ← Adjust analysis parameters
    ├── 4_▶️_Review_and_Run.py      ← Review & launch the pipeline
    ├── 5_📊_Results.py             ← Volcano, PCA, gene table
    └── 6_🔬_Pathway_Analysis.py   ← KEGG/Reactome pathway maps
```

---

## 🧪 Demo mode

Demo mode is **ON by default**. It lets you explore the entire application — including interactive plots and pathway analysis — using built-in synthetic data. No files or Nextflow installation required.

Toggle demo mode **OFF** in the sidebar when you are ready to use your own data.

---

## 🤝 Community & support

- [nf-core community](https://nf-co.re) — the pipeline developers
- [nf-core Slack](https://nf-co.re/join/slack) — ask bioinformatics questions
- [Nextflow docs](https://www.nextflow.io/docs/latest/)

---

## 📄 Licence

MIT — free to use, modify, and share.
