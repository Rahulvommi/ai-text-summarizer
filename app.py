import streamlit as st
from main import summarize_text, extract_keywords, generate_title, humanize_text
import PyPDF2

st.set_page_config(page_title="AI Text Summarizer", page_icon="🧠")

st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
.stTextArea textarea {
    background-color: #1c1e26;
    color: white;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    padding: 10px;
}
.stDownloadButton>button {
    background-color: #2196F3;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 AI Text Summarizer Pro")
st.markdown("### ✨ No word limit • Free • Fast")

text = st.text_area("Enter your text here:")

uploaded_file = st.file_uploader("Or upload a file (.txt or .pdf)", type=["txt", "pdf"])

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text()

summary_type = st.selectbox(
    "Select summary type",
    ["Short", "Medium", "Detailed"]
)

if summary_type == "Short":
    length = 2
elif summary_type == "Medium":
    length = 5
else:
    length = 10   

humanize = st.checkbox("Make summary more human-like")

if st.button("Summarize"):
    if text:
        summary = summarize_text(text, length)

        if humanize:
            summary = humanize_text(summary)

        st.markdown("## ✨ Summary Output")
        st.success(summary)

        keywords = extract_keywords(text)

        st.markdown(f"""
        <div style="
            background-color:#1c1e26;
            padding:15px;
            border-radius:10px;
            margin-top:10px;
        ">
        📊 <b>Original words:</b> {len(text.split())}<br><br>
        ✂️ <b>Summary words:</b> {len(summary.split())}<br><br>
        🔑 <b>Keywords:</b> {", ".join(keywords)}
        </div>
        """, unsafe_allow_html=True)

        title = generate_title(text)
        st.write("📝 Suggested Title:", title)

        st.download_button("Download Summary", summary, file_name="summary.txt")
    else:
        st.warning("Please enter some text or upload a file")

st.divider()
st.markdown("## ⚙️ How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='background-color:#1c1e26; padding:20px; border-radius:12px; text-align:center'>
        <h3>📄 Input</h3>
        <p><b>Paste text</b> or upload <b>.txt / .pdf</b> files</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background-color:#1c1e26; padding:20px; border-radius:12px; text-align:center'>
        <h3>🎯 Process</h3>
        <p>Select <b>Short / Medium / Detailed</b> and click <b>Summarize</b></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background-color:#1c1e26; padding:20px; border-radius:12px; text-align:center'>
        <h3>🚀 Output</h3>
        <p>Get <b>instant summary</b> with keywords & title</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<hr style="margin-top:40px;">

<div style="text-align:center; font-size:15px; color:#aaa;">
    🚀 Built by <b>Rahul</b> | 
    <a href="https://www.linkedin.com/in/vommi-raghavendra-srinivasa-rahul-5aa77b293" target="_blank" style="color:#4CAF50;">
    LinkedIn Profile
    </a>
</div>
""", unsafe_allow_html=True)
