from pinecone import Pinecone
import pdfplumber
import requests
import tempfile


PINECONE_API_KEY="pcsk_3X8XUZ_RSpbXcrtAba1gUeYBCmvKwaZQN7S8RvvXHcUGScsWnbw4Z45CUwW1jRcmSTApYz"

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "jajab-yaya"
if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model":"llama-text-embed-v2",
            "field_map":{"text": "chunk_text"}
        }
    )

def download_pdf_from_url(url):
    response = requests.get(url)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(response.content)
        return tmp.name
    

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=300):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]



def upsert_chunks_to_pinecone(chunks):
    pinecone_vectors=[]
    for i,chunk in enumerate(chunks):
        lol={
                "_id":f"chunk-{i}" ,
                "chunk_text": chunk
            }
        pinecone_vectors.append(lol)

    dense_index = pc.Index(index_name)

    # Upsert the records into a namespace
    dense_index.upsert_records("example-namespace", pinecone_vectors)

    import time
    time.sleep(5)  

    stats = dense_index.describe_index_stats()
    print(stats)
    return dense_index


def search_pinecone(q, dense_index):
    # results = my_index.query(vector=query_embedding, top_k=top_k, include_metadata=True, namespace=namespace)
    # return [match['metadata']['text'] for match in results['matches']]

    ans=[]
    results = dense_index.search(
    namespace="example-namespace",
    query={
        "top_k": 3,
        "inputs": {
            'text': q
        }
    }
    )
    for hit in results['result']['hits']:
        print(f"{hit['fields']['chunk_text']:<50}")
        ans.append(f"{hit['fields']['chunk_text']:<50}")

    return ans


def get_relevant_chunks(url,questions):
    path=download_pdf_from_url(url)
    # path=r"C:\Users\hperu\jajab\pdf.pdf"

    text = extract_text_from_pdf(path)
    # print(text)
    print("************************************************************************************")
    chunks = chunk_text(text)
    # print(chunks)
    
    dense_index=upsert_chunks_to_pinecone(chunks)

    output = {}
    for q in questions:
        # top_chunks = search_pinecone(q, namespace, dense_index)
        ans=search_pinecone(q, dense_index)
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




