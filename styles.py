GLOBAL_CSS = """
<style>
/* ── Reset & base ─────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* Main container */
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Top navigation bar ───────────────────────────────── */
.topnav {
    background: #ffffff;
    border-bottom: 1px solid #E2E8F0;
    padding: 0 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 64px;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}

.topnav-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.25rem;
    font-weight: 700;
    color: #1E40AF;
    text-decoration: none;
}

/* ── Page header ──────────────────────────────────────── */
.page-header {
    background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #3B82F6 100%);
    padding: 3rem 3rem 2.5rem;
    color: white;
}

.page-header h1 {
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    color: white;
}

.page-header p {
    font-size: 1.05rem;
    opacity: 0.88;
    margin: 0;
    color: white;
    max-width: 600px;
}

/* ── Step pill ────────────────────────────────────────── */
.step-pill {
    display: inline-flex;
    align-items: center;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 999px;
    padding: 4px 14px;
    font-size: 0.82rem;
    font-weight: 500;
    color: white;
    margin-bottom: 1rem;
}

/* ── Content wrapper ─────────────────────────────────── */
.content-wrap {
    padding: 2rem 3rem;
    max-width: 1100px;
    margin: 0 auto;
}

/* ── Cards ────────────────────────────────────────────── */
.pipeline-card {
    border: 2px solid #E2E8F0;
    border-radius: 16px;
    padding: 1.4rem 1.5rem;
    background: #ffffff;
    cursor: pointer;
    transition: all 0.2s ease;
    height: 100%;
    position: relative;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.pipeline-card:hover {
    border-color: #93C5FD;
    box-shadow: 0 4px 16px rgba(37,99,235,0.12);
    transform: translateY(-2px);
}

.pipeline-card.selected {
    border-color: #2563EB;
    background: #EFF6FF;
    box-shadow: 0 4px 16px rgba(37,99,235,0.18);
}

.card-icon {
    font-size: 2.2rem;
    margin-bottom: 0.75rem;
    display: block;
}

.card-title {
    font-size: 1.05rem;
    font-weight: 600;
    color: #0F172A;
    margin-bottom: 0.35rem;
}

.card-body {
    font-size: 0.88rem;
    color: #64748B;
    line-height: 1.55;
}

.card-badge {
    position: absolute;
    top: 14px;
    right: 14px;
    background: #2563EB;
    color: white;
    font-size: 0.72rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 999px;
    letter-spacing: 0.02em;
}

/* ── Info / tip box ───────────────────────────────────── */
.tip-box {
    background: #EFF6FF;
    border-left: 4px solid #2563EB;
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.25rem;
    margin: 1rem 0;
    font-size: 0.9rem;
    color: #1E40AF;
    line-height: 1.6;
}

.tip-box strong { color: #1E3A8A; }

/* ── Section heading ─────────────────────────────────── */
.section-heading {
    font-size: 1.05rem;
    font-weight: 600;
    color: #0F172A;
    margin: 1.75rem 0 0.75rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #E2E8F0;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* ── Metric cards ─────────────────────────────────────── */
.metric-card {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 1.1rem 1.25rem;
    text-align: center;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #1E40AF;
    line-height: 1.1;
}

.metric-value.up { color: #DC2626; }
.metric-value.down { color: #2563EB; }
.metric-value.green { color: #059669; }

.metric-label {
    font-size: 0.82rem;
    color: #64748B;
    margin-top: 4px;
    font-weight: 500;
}

/* ── Code block ──────────────────────────────────────── */
.cmd-block {
    background: #0F172A;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    font-family: 'Courier New', monospace;
    font-size: 0.88rem;
    color: #94A3B8;
    line-height: 1.75;
    overflow-x: auto;
}

.cmd-keyword { color: #7DD3FC; }
.cmd-flag    { color: #86EFAC; }
.cmd-value   { color: #FCD34D; }
.cmd-comment { color: #475569; }

/* ── Progress step indicator ─────────────────────────── */
.steps-container {
    display: flex;
    align-items: center;
    gap: 0;
    padding: 1rem 0;
    overflow-x: auto;
}

.step-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    min-width: 80px;
}

.step-circle {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.85rem;
    font-weight: 600;
}

.step-circle.done   { background: #059669; color: white; }
.step-circle.active { background: #2563EB; color: white; }
.step-circle.todo   { background: #E2E8F0; color: #94A3B8; }

.step-name {
    font-size: 0.7rem;
    color: #64748B;
    text-align: center;
    white-space: nowrap;
    font-weight: 500;
}

.step-connector {
    flex: 1;
    height: 2px;
    background: #E2E8F0;
    min-width: 20px;
    margin-bottom: 18px;
}

.step-connector.done { background: #059669; }

/* ── Result pill tags ─────────────────────────────────── */
.tag-up   { background:#FEE2E2; color:#991B1B; padding:2px 10px; border-radius:999px; font-size:0.78rem; font-weight:600; }
.tag-down { background:#DBEAFE; color:#1E40AF; padding:2px 10px; border-radius:999px; font-size:0.78rem; font-weight:600; }
.tag-ns   { background:#F1F5F9; color:#64748B; padding:2px 10px; border-radius:999px; font-size:0.78rem; font-weight:600; }

/* ── Sidebar overrides ────────────────────────────────── */
[data-testid="stSidebar"] {
    background: #F8FAFC !important;
    border-right: 1px solid #E2E8F0 !important;
}

[data-testid="stSidebarNav"] { display: none; }

/* ── Buttons ──────────────────────────────────────────── */
div.stButton > button[kind="primary"] {
    background: #2563EB !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.75rem !important;
    font-size: 0.95rem !important;
    box-shadow: 0 2px 8px rgba(37,99,235,0.3) !important;
    transition: all 0.2s !important;
}

div.stButton > button[kind="primary"]:hover {
    background: #1D4ED8 !important;
    box-shadow: 0 4px 14px rgba(37,99,235,0.4) !important;
    transform: translateY(-1px);
}

div.stButton > button[kind="secondary"] {
    border-radius: 10px !important;
    font-weight: 500 !important;
    border: 1.5px solid #CBD5E1 !important;
}

/* ── Input fields ─────────────────────────────────────── */
[data-testid="stTextInput"] > div > div > input,
[data-testid="stSelectbox"] > div > div {
    border-radius: 10px !important;
    border-color: #CBD5E1 !important;
}

/* ── Expanders ────────────────────────────────────────── */
[data-testid="stExpander"] {
    border: 1px solid #E2E8F0 !important;
    border-radius: 12px !important;
    overflow: hidden;
}

/* ── Alert overrides ──────────────────────────────────── */
[data-testid="stAlert"] {
    border-radius: 12px !important;
}

/* ── Tabs ─────────────────────────────────────────────── */
button[data-baseweb="tab"] {
    font-size: 0.9rem !important;
    font-weight: 500 !important;
}

/* ── Data editor / table ──────────────────────────────── */
[data-testid="stDataFrame"], [data-testid="stDataEditor"] {
    border-radius: 12px !important;
    overflow: hidden;
    border: 1px solid #E2E8F0 !important;
}

/* ── Footer bar ───────────────────────────────────────── */
.footer-bar {
    background: #F8FAFC;
    border-top: 1px solid #E2E8F0;
    padding: 1.25rem 3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 3rem;
}

.footer-text {
    font-size: 0.82rem;
    color: #94A3B8;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #F1F5F9; }
::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 3px; }
</style>
"""


def page_header(step_num: int, title: str, subtitle: str):
    steps = [
        ("1", "Choose Analysis"),
        ("2", "Your Samples"),
        ("3", "Settings"),
        ("4", "Review & Run"),
        ("5", "Results"),
        ("6", "Pathways"),
    ]
    pills = ""
    connectors_html = ""
    for i, (n, label) in enumerate(steps):
        state = "done" if int(n) < step_num else ("active" if int(n) == step_num else "todo")
        pills += f'<div class="step-item"><div class="step-circle {state}">{"✓" if state=="done" else n}</div><div class="step-name">{label}</div></div>'
        if i < len(steps) - 1:
            conn_state = "done" if int(n) < step_num else ""
            pills += f'<div class="step-connector {conn_state}"></div>'

    import streamlit as st
    st.markdown(
        f"""
        <div class="page-header">
            <div style="max-width:900px;margin:0 auto;">
                <div style="display:flex;align-items:center;gap:12px;margin-bottom:1.25rem;overflow-x:auto;">
                    {pills}
                </div>
                <h1>{title}</h1>
                <p>{subtitle}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def tip(text: str):
    import streamlit as st
    st.markdown(f'<div class="tip-box">💡 {text}</div>', unsafe_allow_html=True)


def section(icon: str, title: str):
    import streamlit as st
    st.markdown(f'<div class="section-heading">{icon} {title}</div>', unsafe_allow_html=True)
