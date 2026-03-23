import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from collections import Counter
import re

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, num_sentences)

    result = ""
    for sentence in summary:
        result += str(sentence) + " "

    return result


def extract_keywords(text, num=5):
    words = re.findall(r'\w+', text.lower())
    common = Counter(words).most_common(num)
    return [word for word, _ in common]


def generate_title(text):
    sentences = text.split(".")
    return sentences[0][:60] + "..."
def generate_title(text):
    sentences = text.split(".")
    return sentences[0][:60] + "..."


# 🔹 HUMANIZE FUNCTION (PASTE HERE)
def humanize_text(text):
    replacements = {
        "However": "But",
        "In addition": "Also",
        "Moreover": "Besides",
        "Therefore": "So",
        "Thus": "So",
        "Additionally": "Plus",
        "It helps in": "It makes it easier to",
        "Many industries": "A lot of industries",
    }

    for key, value in replacements.items():
        text = text.replace(key, value)

    return text


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        text = file.read()

    result = summarize_text(text)

    with open("output.txt", "w") as file:
        file.write(result)

    print("Summary saved to output.txt")
    print(result)
