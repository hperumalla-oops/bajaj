import openai

# Assume the async client is initialized as in the previous example
client = openai.AsyncOpenAI(api_key="")

async def async_ask_openai(context: str, question: str) -> str:
    """
    An asynchronous function that asks OpenAI a question based on context.
    - It uses a specific prompt structure.
    - It's designed for concurrent execution.
    """
    # The system message sets the behavior and constraints for the AI
    system_prompt = """
You are an expert assistant answering a question based on the provided context.
- Your answer must not exceed 50 words.
- Do NOT add any disclaimers or explanations outside of the answer itself.
    """

    # The user message contains the specific data for this single request
    user_prompt = f"""
Context:
{context}

Question:
{question}
"""

    try:
        # Use the await keyword to make the non-blocking API call
        chat_completion = await client.chat.completions.create(
            # Note: "gpt-4.1-nano" might be a hypothetical model.
            # Use a real model name like "gpt-4o-mini" or "gpt-4-turbo" if it doesn't work.
            model="gpt-4.1-nano", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )
        # The way to get the output text is different in the standard client
        return chat_completion.choices[0].message.content

    except Exception as e:
        print(f"An error occurred for question '{question}': {e}")
        # Return an empty string or a custom error message
        return "Error processing request."