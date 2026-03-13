import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load documents
with open("semantic-search-ai/documents.txt") as f:
    docs = [line.strip() for line in f.readlines()]

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(docs).toarray()

# Load vector database
with open("semantic-search-ai/vector_db.json") as f:
    db = json.load(f)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query):

    query_vector = vectorizer.transform([query]).toarray()[0]

    scores = []

    for item in db:
        score = cosine_similarity(query_vector, item["vector"])
        scores.append((score, item["text"]))

    scores.sort(reverse=True)

    return [s[1] for s in scores[:2]]