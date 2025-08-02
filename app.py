from pydantic import BaseModel
from retriever import get_relevant_chunks
from model import ask_gemini
import uvicorn

app = FastAPI()

class RAGRequest(BaseModel):
    documents: str  # PDF URL
    questions: list[str]

@app.post("/hackrx/run")
async def run_rag(request: RAGRequest):
    chunks = get_relevant_chunks(request.documents, request.questions)
    responses = []
    for q in request.questions:
        context = chunks.get(q, "")
        lol = ask_gemini(context, q)
        answer = lol.text.strip() if lol.text else "No answer found."
        responses.append(answer)
        
    return {"answers": responses}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)


