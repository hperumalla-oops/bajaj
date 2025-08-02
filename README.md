# bajaj
LLM-Powered Intelligent Query–Retrieval System 


put this in your cmd to test

```
curl -X POST http://localhost:8000/hackrx/run -H "Content-Type: application/json" -d "{\"documents\": \"https://arxiv.org/pdf/1706.03762.pdf\", \"questions\": [\"What is the transformer architecture?\", \"Why is self-attention important?\"]}"

```
or this in postman

`http://localhost:8000/hackrx/run`
```
{
  "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
  "questions": [
    "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
    "What is the waiting period for pre-existing diseases (PED) to be covered?",
    "Does this policy cover maternity expenses, and what are the conditions?",
    "What is the waiting period for cataract surgery?",
    "Are the medical expenses for an organ donor covered under this policy?",
    "What is the No Claim Discount (NCD) offered in this policy?",
    "Is there a benefit for preventive health check-ups?",
    "How does the policy define a 'Hospital'?",
    "What is the extent of coverage for AYUSH treatments?",
    "Are there any sub-limits on room rent and ICU charges for Plan A?"
  ]
}
```




after cloning, change the api key in the .env file
