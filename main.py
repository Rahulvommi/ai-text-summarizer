import re
from collections import Counter

def summarize_text(text, length=3):
    text = text.replace("\n", " ")

    sentences = re.split(r'(?<=[.!?]) +', text)

    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

    if not sentences:
        return "No meaningful content to summarize."

    return " ".join(sentences[:length])


def extract_keywords(text, num_keywords=5):
    words = re.findall(r'\w+', text.lower())

    stopwords = set([
        "the","is","in","and","to","of","a","for","on","with",
        "as","by","an","be","are","this","that","it","from","at"
    ])

    filtered = [w for w in words if w not in stopwords and len(w) > 3]

    freq = Counter(filtered)
    keywords = [word for word, _ in freq.most_common(num_keywords)]

    return keywords


def generate_title(text):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())

    if sentences:
        return sentences[0][:60] + "..."
    return "Generated Title"


def humanize_text(text):
    return text.replace("This", "This clearly").replace("In conclusion", "To sum up")
