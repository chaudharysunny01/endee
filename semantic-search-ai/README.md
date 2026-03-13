# AI Semantic Search using Vector Database

## Overview
This project demonstrates a semantic search system using vector embeddings.

## Problem Statement
Traditional keyword search cannot understand semantic meaning in text. This project implements a vector-based search system to retrieve relevant documents.

## Technical Approach
1. Documents are converted into vector embeddings using TF-IDF.
2. Vectors are stored in a vector database.
3. User queries are converted into embeddings.
4. Cosine similarity is used to find the most relevant documents.

## Technologies Used
- Python
- Scikit-learn
- Streamlit
- Vector embeddings

## How Endee is Used
The project is built inside the forked Endee repository and demonstrates vector-based search functionality similar to modern vector database workflows.

## Running the Project

Install dependencies:

pip install scikit-learn numpy streamlit

Run embedding script:

python semantic-search-ai/embed_store.py

Start the application:

streamlit run semantic-search-ai/app.py
