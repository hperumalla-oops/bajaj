print("it shratteddd")
import chromadb
print("imported chroma db")
from chromadb.config import Settings
print("got settign from crhoma db")


from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

print("imported sentr trans")
print("model is loaded")



import numpy as np

from utils import *

chroma_client = chromadb.Client(Settings())
print("client initialized")
# model = SentenceTransformer('all-MiniLM-L6-v2')  # Or any embedding model

def upsert_chunks_to_chroma(chunks):
    collection = chroma_client.get_or_create_collection(name="example")

    ids = [f"chunk-{i}" for i in range(len(chunks))]
    embeddings = model.encode(chunks).tolist()

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=[{"chunk_text": chunk} for chunk in chunks]
    )

    # print(f"Inserted {len(chunks)} chunks into ChromaDB.")
    return collection

def search_chroma(q, collection):
    query_embedding = model.encode([q]).tolist()[0]
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        include=['documents', 'metadatas']
    )

    # Print and return matched texts
    matched_chunks = results['documents'][0]
    # for text in matched_chunks:
    #     # print(text)
    
    return matched_chunks


def get_relevant_chunks(url,questions):
    path=download_pdf_from_url(url)
    print("got path")
    text = extract_text_from_pdf(path)
    print("exctred text")
    chunks = chunk_text(text)
    print("chunked")

    collection=upsert_chunks_to_chroma(chunks)

    output = {}
    for q in questions:
        # top_chunks = search_pinecone(q, namespace, dense_index)
        ans=search_chroma(q,collection)
        print("djfisdjfidsjfijdsfujsdifjsdfjidsujfisdfj")
        output[q] = "\n\n".join(ans)
    return output



# questions=[
#         "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
#         "What is the waiting period for pre-existing diseases (PED) to be covered?",
#         "Does this policy cover maternity expenses, and what are the conditions?",
#         "What is the waiting period for cataract surgery?"
     
#     ]
# doc="https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D"

# get_relevant_chunks(doc,questions)

