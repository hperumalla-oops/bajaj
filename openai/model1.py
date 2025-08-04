from openai import OpenAI

client = OpenAI(api_key="")

def ask_openai(dict):
    prompt = f"""
You are answering a question based on a document.
        - you are given a dictionary with question as key and value as context, use this to output a python list of answers in the same order as the questions, 
        - do not repeat the questions in the answer
        - answer all the questions, you can use context from other questions to answer a different questions if required
        - Try to keep it below 50 words and do not explain, keept it brief
        
Dict:
{dict}


Only answer from the context.
"""
    response = client.responses.create(
    model="gpt-4.1-nano",
    input=prompt
    )
    return response.output_text

