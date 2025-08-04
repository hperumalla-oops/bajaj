from openai import OpenAI

client = OpenAI(api_key="")

def ask_openai(context, question):
    prompt = f"""
You are answering a question based on a document.
        - Try to keep it below 50 words
        - keep almost the same sentence structure
        -quote verbatim as much as possible
        - Do NOT add explanations.
        
Context:
{context}

Question:
{question}

Only answer from the context.
"""
    response = client.responses.create(
    model="gpt-4.1-nano",
    input=prompt
    )
    return response.output_text


