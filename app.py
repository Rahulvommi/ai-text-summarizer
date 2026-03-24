import streamlit as st
from main import summarize_text, extract_keywords, generate_title, humanize_text
import PyPDF2

st.set_page_config(page_title="AI Summarizer", layout="wide")

st.markdown("""
<style>
body {
    background: #0a0a0a;
    color: #ffffff;
    font-family: 'Inter', sans-serif;
}

.block-container {
    padding: 2rem 4rem;
}

.hero-title {
    font-size: 56px;
    font-weight: 600;
    letter-spacing: -1px;
}

.hero-sub {
    color: #a1a1a1;
    font-size: 16px;
    margin-bottom: 30px;
}

textarea {
    background:#111 !important;
    border-radius:14px !important;
    border:1px solid #2a2a2a !important;
    color:#fff !important;
}

.stButton > button {
    background:#ffffff;
    color:#000;
    border-radius:999px;
    padding:10px 24px;
    border:none;
}

.stDownloadButton > button {
    background:transparent;
    border:1px solid #444;
    color:#fff;
    border-radius:999px;
}

.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.1);
    padding:20px;
    border-radius:20px;
    margin-top:20px;
}

.section {
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">AI Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Precision text summarization with clean structure.</div>', unsafe_allow_html=True)

text = st.text_area("Enter text")

uploaded_file = st.file_uploader("Upload (.txt / .pdf)", type=["txt", "pdf"])

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text()

col1, col2, col3 = st.columns(3)

with col1:
    summary_type = st.selectbox("Length", ["Short", "Medium", "Detailed"])

with col2:
    humanize = st.checkbox("Refine tone")

with col3:
    run = st.button("Generate")

if summary_type == "Short":
    length = 2
elif summary_type == "Medium":
    length = 5
else:
    length = 10

if run:
    if text:

        summary = summarize_text(text, length)

        if humanize:
            summary = humanize_text(summary)

        st.markdown('<div class="section"></div>', unsafe_allow_html=True)

        col1, col2 = st.columns([2,1])

        with col1:
            st.markdown(f"""
            <div class="glass">

            <div style="display:flex; justify-content:space-between; align-items:center;">
                <b>Summary</b>
                <button onclick="copyText()" 
                    style="background:#fff;color:#000;border:none;padding:6px 14px;border-radius:999px;cursor:pointer;font-size:12px;">
                    Copy
                </button>
            </div>

            <p id="summary-text" style="margin-top:15px;">
            {summary}
            </p>

            </div>

            <script>
            function copyText() {{
                var text = document.getElementById("summary-text").innerText;
                navigator.clipboard.writeText(text);
            }}
            </script>
            """, unsafe_allow_html=True)

        with col2:
            keywords = extract_keywords(text)
            title = generate_title(text)

            st.markdown(f"""
            <div class="glass">
            <b>Insights</b><br><br>
            Words (original): {len(text.split())}<br><br>
            Words (summary): {len(summary.split())}<br><br>
            Keywords: {", ".join(keywords)}<br><br>
            Title: {title}
            </div>
            """, unsafe_allow_html=True)

        st.download_button("Download Summary", summary, file_name="summary.txt")

    else:
        st.warning("Please provide input text.")

st.markdown(
    """
    <div style="text-align:center; margin-top:60px;">
    <br><br><br>
 Rahul Vommi
 <br>
        Check Out My_<a href="https://foliofyx.in/portfolio/rahulvommi"
                  target="_blank"
                  style="color:#bbb; text-decoration:underline;">
                  Portfolio
               </a>


    """,
    unsafe_allow_html=True
)
