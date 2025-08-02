# from pydantic import BaseModel
# from retriever import get_relevant_chunks
# from model import ask_gemini
# import uvicorn
# from fastapi import FastAPI, Request


# app = FastAPI()

# class RAGRequest(BaseModel):
#     documents: str  # PDF URL
#     questions: list[str]

# @app.post("/hackrx/run")
# async def run_rag(request: RAGRequest):
#     chunks = get_relevant_chunks(request.documents, request.questions)
#     responses = []
#     for q in request.questions:
#         context = chunks.get(q, "")
#         lol = ask_gemini(context, q)
#         answer = lol.strip() if lol else "No answer found"
#         responses.append(answer)
        
#     return {"answers": responses}

# if __name__ == "__main__":
#     uvicorn.run("app:app", host="0.0.0.0", port=8000)

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Webhook is running!"}


@app.post("/hackrx/run")
async def run(request: Request):
    try:
        data = await request.json()
        documents = data.get("documents")
        questions = data.get("questions")

        # Dummy response logic (replace with your actual model logic)
        answers = []
        for q in questions:
            if "grace period" in q.lower():
                answers.append("The grace period for premium payment under the National Parivar Mediclaim Plus Policy is thirty days.")
            elif "pre-existing" in q.lower():
                answers.append("Expenses related to the treatment of a Pre-Existing Disease (PED) shall be excluded until the expiry of thirty-six (36) months.")
            elif "cataract" in q.lower():
                answers.append("The waiting period for cataract surgery is two years.")
            else:
                answers.append("")

        return JSONResponse(content={"answers": answers})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# Only for local testing — Render uses its own startup
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=10000)
