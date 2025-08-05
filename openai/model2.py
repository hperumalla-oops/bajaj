import openai


client = openai.AsyncOpenAI(api_key="")

async def async_ask_openai(context: str, question: str) -> str:

  
    system_prompt = """
        - Try to keep it below 50 words
        - keep almost the same sentence structure
        - quote verbatim as much as possible
        - Do NOT add explanations.
    """

    
    user_prompt = f"""
Context:
{context}

Question:
{question}
"""

    try:
        
        chat_completion = await client.chat.completions.create(
            
            model="gpt-4.1-nano", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )
       
        return chat_completion.choices[0].message.content

    except Exception as e:
        print(f"An error occurred for question '{question}': {e}")
       

        return "Error processing request."
