from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma

class LocalEmbeddingFunction:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()
    def embed_query(self, text):
        return self.model.encode([text]).tolist()[0]

embedding_function = LocalEmbeddingFunction()

def build_vector_store(texts):
    return Chroma.from_texts(texts, embedding=embedding_function, persist_directory="./chroma_db")

def hybrid_retrieve(query, vector_db, top_k=2):
    return vector_db.similarity_search(query, k=top_k)
