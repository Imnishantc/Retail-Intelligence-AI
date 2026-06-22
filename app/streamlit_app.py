import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate

from chart_generator import generate_chart
from prompts import SQL_PROMPT
from query_executor import execute_query
from explanation_generator import generate_explanation

load_dotenv()

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI SQL Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

.stApp {
    background: #070C18 !important;
    font-family: 'Inter', sans-serif;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Hero Banner ── */
.hero {
    background: linear-gradient(135deg, #0D1526 0%, #0A1020 50%, #0D1A2E 100%);
    border-bottom: 1px solid rgba(59,130,246,0.15);
    padding: 52px 60px 44px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -80px; left: -80px;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(59,130,246,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -60px; right: 100px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(16,185,129,0.05) 0%, transparent 70%);
    pointer-events: none;
}
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(59,130,246,0.1);
    border: 1px solid rgba(59,130,246,0.25);
    border-radius: 100px;
    padding: 4px 14px 4px 10px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #60A5FA;
    margin-bottom: 20px;
}
.hero-eyebrow .dot {
    width: 6px; height: 6px;
    background: #3B82F6;
    border-radius: 50%;
    animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 42px;
    font-weight: 700;
    color: #F0F4FF;
    margin: 0 0 10px;
    letter-spacing: -0.02em;
    line-height: 1.15;
}
.hero-title span {
    background: linear-gradient(90deg, #3B82F6, #60A5FA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 16px;
    color: #64748B;
    margin: 0;
    font-weight: 400;
    letter-spacing: 0.01em;
}

/* ── Main Content Area ── */
.main-content {
    padding: 40px 60px;
    max-width: 1100px;
    margin: 0 auto;
}

/* ── Input Section ── */
.input-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 10px;
}

/* Streamlit text_input override */
div[data-testid="stTextInput"] > div > div > input {
    background: #0F1829 !important;
    border: 1.5px solid #1E2D45 !important;
    border-radius: 10px !important;
    color: #E2E8F0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    padding: 14px 18px !important;
    height: auto !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
div[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #3B82F6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.12) !important;
    outline: none !important;
}
div[data-testid="stTextInput"] > div > div > input::placeholder {
    color: #334155 !important;
}

/* ── Analyze Button ── */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #2563EB, #3B82F6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 13px 32px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 20px rgba(59,130,246,0.3) !important;
    width: 100% !important;
}
div[data-testid="stButton"] > button:hover {
    background: linear-gradient(135deg, #1D4ED8, #2563EB) !important;
    box-shadow: 0 6px 28px rgba(59,130,246,0.45) !important;
    transform: translateY(-1px) !important;
}
div[data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
}

/* ── Pipeline Steps ── */
.pipeline {
    display: flex;
    align-items: center;
    gap: 0;
    margin: 36px 0 32px;
}
.pipeline-step {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    position: relative;
}
.pipeline-step::after {
    content: '';
    position: absolute;
    top: 16px;
    left: calc(50% + 20px);
    right: calc(-50% + 20px);
    height: 1px;
    background: linear-gradient(90deg, #1E3A5F, #1E3A5F);
}
.pipeline-step:last-child::after { display: none; }
.pipeline-icon {
    width: 36px; height: 36px;
    border-radius: 50%;
    background: #0F1829;
    border: 1.5px solid #1E2D45;
    display: flex; align-items: center; justify-content: center;
    font-size: 15px;
    position: relative; z-index: 1;
    transition: all 0.3s;
}
.pipeline-icon.active {
    background: rgba(59,130,246,0.12);
    border-color: #3B82F6;
    box-shadow: 0 0 16px rgba(59,130,246,0.3);
}
.pipeline-icon.done {
    background: rgba(16,185,129,0.1);
    border-color: #10B981;
}
.pipeline-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #334155;
    font-family: 'Space Grotesk', sans-serif;
}
.pipeline-label.active { color: #60A5FA; }
.pipeline-label.done { color: #34D399; }

/* ── Result Cards ── */
.result-card {
    background: #0C1526;
    border: 1px solid #1A2840;
    border-radius: 14px;
    padding: 28px 30px;
    margin-bottom: 20px;
}
.card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 16px;
}
.card-icon {
    width: 32px; height: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 15px;
}
.card-icon.blue { background: rgba(59,130,246,0.12); }
.card-icon.green { background: rgba(16,185,129,0.10); }
.card-icon.purple { background: rgba(139,92,246,0.10); }
.card-icon.orange { background: rgba(249,115,22,0.10); }
.card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #475569;
    margin: 0;
}

/* ── SQL Code Block ── */
div[data-testid="stCode"] {
    background: #060C18 !important;
    border: 1px solid #1A2840 !important;
    border-radius: 10px !important;
}
div[data-testid="stCode"] pre {
    background: transparent !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
    line-height: 1.6 !important;
    color: #94A3B8 !important;
    padding: 18px 20px !important;
}

/* ── Dataframe ── */
div[data-testid="stDataFrame"] {
    border: 1px solid #1A2840 !important;
    border-radius: 10px !important;
    overflow: hidden !important;
}
div[data-testid="stDataFrame"] iframe {
    border-radius: 10px !important;
}

/* ── Subheaders – hide default, we use custom ── */
h2[data-testid="stHeading"] { display: none !important; }

/* ── Spinner ── */
div[data-testid="stSpinner"] > div {
    color: #3B82F6 !important;
}

/* ── Error ── */
div[data-testid="stAlert"] {
    background: rgba(239,68,68,0.08) !important;
    border: 1px solid rgba(239,68,68,0.25) !important;
    border-radius: 10px !important;
    color: #FCA5A5 !important;
}

/* ── Business Insight Text ── */
.insight-text {
    font-size: 15px;
    line-height: 1.75;
    color: #94A3B8;
    font-weight: 400;
}

/* ── Divider ── */
.section-divider {
    border: none;
    border-top: 1px solid #111A2C;
    margin: 8px 0 24px;
}

/* ── Spacing helpers ── */
.spacer-sm { margin-bottom: 12px; }
.spacer-md { margin-bottom: 24px; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow"><span class="dot"></span>Powered by Mistral AI</div>
    <h1 class="hero-title">AI <span>SQL</span> Analyst</h1>
    <p class="hero-sub">Ask any business question in plain English — get SQL, results, and insight instantly.</p>
</div>
""", unsafe_allow_html=True)

# ── Main Content ──────────────────────────────────────────────────────────────
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# ── LLM Setup ────────────────────────────────────────────────────────────────
llm = ChatMistralAI(model="mistral-small-latest", temperature=0)
prompt = PromptTemplate(input_variables=["question"], template=SQL_PROMPT)
chain = prompt | llm

# ── Input Row ─────────────────────────────────────────────────────────────────
col_input, col_btn = st.columns([5, 1])
with col_input:
    st.markdown('<div class="input-label">Your question</div>', unsafe_allow_html=True)
    question = st.text_input(
        label="question",
        label_visibility="collapsed",
        placeholder="e.g. What were the top 5 products by revenue last quarter?",
    )
with col_btn:
    st.markdown('<div class="input-label">&nbsp;</div>', unsafe_allow_html=True)
    analyze = st.button("Analyze →")

# ── Pipeline Indicator ────────────────────────────────────────────────────────
if analyze and question:
    st.markdown("""
    <div class="pipeline">
        <div class="pipeline-step">
            <div class="pipeline-icon active">🧠</div>
            <div class="pipeline-label active">Generate SQL</div>
        </div>
        <div class="pipeline-step">
            <div class="pipeline-icon">⚡</div>
            <div class="pipeline-label">Run Query</div>
        </div>
        <div class="pipeline-step">
            <div class="pipeline-icon">💡</div>
            <div class="pipeline-label">Explain</div>
        </div>
        <div class="pipeline-step">
            <div class="pipeline-icon">📊</div>
            <div class="pipeline-label">Visualize</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Step 1: Generate SQL ──────────────────────────────────────────────────
    with st.spinner("Generating SQL query…"):
        response = chain.invoke({"question": question})
        sql_query = (
            response.content
            .replace("```sql", "")
            .replace("```", "")
            .strip()
        )
        sql_query = sql_query.replace("retaildb.retail_sales", "retail_sales")

    st.markdown("""
    <div class="result-card">
        <div class="card-header">
            <div class="card-icon blue">🔷</div>
            <p class="card-title">Generated SQL</p>
        </div>
        <hr class="section-divider">
    </div>
    """, unsafe_allow_html=True)
    # Render code outside the HTML card div so Streamlit can process it
    st.code(sql_query, language="sql")

    # ── Step 2: Execute ───────────────────────────────────────────────────────
    try:
        with st.spinner("Running query against database…"):
            result = execute_query(sql_query)
    except Exception as e:
        st.error(f"Query failed: {e}")
        st.stop()

    st.markdown("""
    <div class="result-card">
        <div class="card-header">
            <div class="card-icon green">📋</div>
            <p class="card-title">Query Results</p>
        </div>
        <hr class="section-divider">
    </div>
    """, unsafe_allow_html=True)
    st.dataframe(result, use_container_width=True)

    # ── Step 3: Explain ───────────────────────────────────────────────────────
    with st.spinner("Generating business insight…"):
        explanation = generate_explanation(question, result.to_string())

    st.markdown(f"""
    <div class="result-card">
        <div class="card-header">
            <div class="card-icon purple">💡</div>
            <p class="card-title">Business Insight</p>
        </div>
        <hr class="section-divider">
        <p class="insight-text">{explanation}</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Step 4: Chart ─────────────────────────────────────────────────────────
    if len(result.columns) >= 2 and len(result) > 1:
        st.markdown("""
        <div class="result-card">
            <div class="card-header">
                <div class="card-icon orange">📈</div>
                <p class="card-title">Visualization</p>
            </div>
            <hr class="section-divider">
        </div>
        """, unsafe_allow_html=True)
        generate_chart(result)

elif analyze and not question:
    st.warning("Please enter a business question before analyzing.")

st.markdown('</div>', unsafe_allow_html=True)  # close main-content