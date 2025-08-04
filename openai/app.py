from pydantic import BaseModel
from retriever import get_relevant_chunks

from model1 import ask_openai
import json
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

class RAGRequest(BaseModel):
    documents: str  # PDF URL
    questions: list[str]

con_dict={}

@app.post("/hackrx/run")
async def run_rag(request: RAGRequest):
    chunks = get_relevant_chunks(request.documents, request.questions)
    responses = []
    for q in request.questions:
        context = chunks.get(q, "")
        con_dict[q] = context
        
    responses = ask_openai(con_dict)

    #with open("question_context_map.json", "w", encoding="utf-8") as f:
        #json.dump(con_dict, f, ensure_ascii=False, indent=4)

    
    return {"answers":responses}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)


