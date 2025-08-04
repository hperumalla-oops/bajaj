import requests
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tempfile

from utils import chunk_text


def download_pdf_from_url(url):
    response = requests.get(url)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(response.content)
        return tmp.name

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def get_relevant_chunks(url, questions):
    path = download_pdf_from_url(url)
    text = extract_text_from_pdf(path)
    chunks = chunk_text(text, chunk_size=150)

    vectorizer = TfidfVectorizer().fit(chunks + questions)
    chunk_vectors = vectorizer.transform(chunks)
    question_vectors = vectorizer.transform(questions)

    results = {}
    for i, q in enumerate(questions):
        sims = cosine_similarity(question_vectors[i], chunk_vectors).flatten()
        top_idx = sims.argsort()[-3:][::-1]
        context = "\n\n".join([chunks[j] for j in top_idx])
        results[q] = context
    return results
