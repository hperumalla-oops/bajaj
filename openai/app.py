from pydantic import BaseModel
from retriever import get_relevant_chunks
#from chroma_db import get_relevant_chunks
import time
from model2 import async_ask_openai
import json
import uvicorn
from fastapi import FastAPI, Request
import asyncio

print("new")
app = FastAPI()

class RAGRequest(BaseModel):
    documents: str  
    questions: list[str]



async def get_openai_responses_concurrently(questions: list[str], chunks: dict) -> list[str]:
    """Gathers all API call tasks and runs them in parallel."""
    tasks = []
    for q in questions:
        context = chunks.get(q, "")
        task = asyncio.create_task(async_ask_openai(context, q))
        tasks.append(task)
    
    
    results = await asyncio.gather(*tasks)
    
   
    final_answers = [res.strip() if res else "No answer found" for res in results]
    return final_answers



@app.post("/hackrx/run")
async def run_rag(request: RAGRequest):
    full_start_time = time.perf_counter()

   
    chunk_start_time = time.perf_counter()
    
   
    chunks = await asyncio.to_thread(get_relevant_chunks, request.documents, request.questions)
    
    chunk_end_time = time.perf_counter()
    print(f"Chunk Function executed in: {chunk_end_time - chunk_start_time:.6f} seconds")

   
    api_start_time = time.perf_counter()
    
   
    responses = await get_openai_responses_concurrently(request.questions, chunks)
    
    api_end_time = time.perf_counter()
    print("new")
    print(f"API Function (Concurrent) executed in: {api_end_time - api_start_time:.6f} seconds")

  
    full_end_time = time.perf_counter()
    print(f"Full Function executed in: {full_end_time - full_start_time:.6f} seconds")

    return {"success": True, "answers": responses}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)


