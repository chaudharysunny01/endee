from sklearn.feature_extraction.text import TfidfVectorizer
import json

# Load documents
with open("semantic-search-ai/documents.txt") as f:
    docs = [line.strip() for line in f.readlines()]

# Create embeddings
vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(docs).toarray()

# Save vectors locally (simulating vector database storage)
data = []

for i, doc in enumerate(docs):
    data.append({
        "id": i,
        "text": doc,
        "vector": embeddings[i].tolist()
    })

# Save vector database file
with open("semantic-search-ai/vector_db.json", "w") as f:
    json.dump(data, f)

print("Vector database created successfully.")