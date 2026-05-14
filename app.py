"""
BioFlow — Home page
"""
import streamlit as st
from styles import GLOBAL_CSS

st.set_page_config(
    page_title="BioFlow — Genomics for Everyone",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Session state defaults ────────────────────────────────────────────────────
DEFAULTS = {
    "pipeline": None,
    "genome": "GRCh38",
    "genome_label": "Human (Homo sapiens) — hg38 / GRCh38",
    "condition_a": "Control",
    "condition_b": "Treated",
    "samplesheet": None,
    "padj_cutoff": 0.05,
    "lfc_cutoff": 1.0,
    "outdir": "./results",
    "profile": "docker",
    "demo_mode": True,
    "run_complete": False,
    "pathway_db": "KEGG_2021_Human",
    "deseq_results": None,
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Hero banner ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#1E3A8A 0%,#2563EB 55%,#3B82F6 100%);
     padding:4rem 3rem 3.5rem;text-align:center;color:white;">
    <div style="font-size:3.5rem;margin-bottom:1rem;">🧬</div>
    <h1 style="font-size:2.6rem;font-weight:800;margin:0 0 0.75rem;color:white;letter-spacing:-0.02em;">
        BioFlow
    </h1>
    <p style="font-size:1.2rem;opacity:0.9;max-width:600px;margin:0 auto 0.5rem;color:white;line-height:1.6;">
        Run professional genomics analysis without writing a single line of code.
    </p>
    <p style="font-size:0.95rem;opacity:0.72;color:white;margin:0;">
        Built on <strong>nf-core</strong> — the gold standard in bioinformatics pipelines.
    </p>
</div>
""", unsafe_allow_html=True)

# ── What is this tool? ────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem 1rem;">
        <div style="font-size:2.5rem;margin-bottom:0.75rem;">🖱️</div>
        <div style="font-weight:700;font-size:1.05rem;color:#0F172A;margin-bottom:0.4rem;">Point & Click</div>
        <div style="font-size:0.88rem;color:#64748B;line-height:1.6;">
            No command line, no scripts. Fill in a form, upload your files, click Run.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem 1rem;">
        <div style="font-size:2.5rem;margin-bottom:0.75rem;">🔬</div>
        <div style="font-weight:700;font-size:1.05rem;color:#0F172A;margin-bottom:0.4rem;">Publication-Ready Results</div>
        <div style="font-size:0.88rem;color:#64748B;line-height:1.6;">
            Volcano plots, PCA, pathway maps — all downloadable and ready for your paper.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem 1rem;">
        <div style="font-size:2.5rem;margin-bottom:0.75rem;">✅</div>
        <div style="font-weight:700;font-size:1.05rem;color:#0F172A;margin-bottom:0.4rem;">Community Validated</div>
        <div style="font-size:0.88rem;color:#64748B;line-height:1.6;">
            Powered by nf-core — used by thousands of research labs worldwide.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border:none;border-top:1px solid #E2E8F0;margin:0.5rem 3rem 2rem'>", unsafe_allow_html=True)

# ── Help me pick ──────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-bottom:1.5rem;">
    <h2 style="font-size:1.5rem;font-weight:700;color:#0F172A;margin-bottom:0.35rem;">
        What did you do in the lab?
    </h2>
    <p style="color:#64748B;font-size:0.95rem;">
        Answer one question and we'll take you straight to the right analysis.
    </p>
</div>
""", unsafe_allow_html=True)

CHOICES = {
    "I measured RNA to see which genes are active (RNA-seq)": ("rnaseq", "pages/1_🧬_Choose_Analysis.py"),
    "I sequenced DNA to find mutations or variants (WES/WGS)": ("exome", "pages/1_🧬_Choose_Analysis.py"),
    "I pulled down a protein and sequenced the DNA around it (ChIP-seq)": ("chipseq", "pages/1_🧬_Choose_Analysis.py"),
    "I mapped open chromatin regions in my cells (ATAC-seq)": ("atacseq", "pages/1_🧬_Choose_Analysis.py"),
    "I'm not sure — help me decide": (None, "pages/1_🧬_Choose_Analysis.py"),
}

col_left, col_mid, col_right = st.columns([1, 3, 1])
with col_mid:
    for label, (pipeline_key, page) in CHOICES.items():
        if st.button(label, use_container_width=True, key=f"home_{pipeline_key}"):
            if pipeline_key:
                st.session_state.pipeline = pipeline_key
            st.switch_page(page)

# ── Demo mode banner ──────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
with st.container():
    st.info(
        "🎯 **Demo mode is active.** You can explore the entire app — including results, "
        "plots, and pathway analysis — using built-in example data. "
        "No files or installation needed to get started.",
        icon=None,
    )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:2rem 1rem 1rem;color:#94A3B8;font-size:0.82rem;">
    Built with ❤️ for wet-lab scientists &nbsp;·&nbsp;
    Powered by <a href="https://nf-co.re" target="_blank" style="color:#2563EB;">nf-core</a> &nbsp;·&nbsp;
    <a href="https://www.nextflow.io" target="_blank" style="color:#2563EB;">Nextflow</a>
</div>
""", unsafe_allow_html=True)
