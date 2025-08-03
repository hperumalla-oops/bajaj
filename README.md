# jajab
nfekjnfkjenjnwefnjn

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



current o/p looks like this
```
{
    "answers": [
        "The grace period for premium payment is thirty days.",
        "Expenses related to the treatment of a Pre-Existing Disease (PED) and its direct complications shall be excluded until the expiry of thirty-six (36) months of continuous coverage after the date of inception of the first policy.",
        "Yes, maternity expenses are covered if the female insured has been continuously covered for at least 24 months. Ectopic pregnancy is included if medically established. Exclusions apply, such as age limits (below 18, above 45) and a 24-month waiting period for delivery/termination (except accident).",
        "The waiting period for cataract surgery is two years.",
        "Yes, the medical expenses incurred for an organ donor's hospitalization during the policy period for harvesting an organ donated to an Insured Person are covered, provided the donation conforms to the Transplantation of Human Organs Act 1994 and other specified conditions.",
        "A flat 5% No Claim Discount (NCD) is allowed on the base premium for renewal of policies with a term of one year, provided claims are not reported in the expiring policy. For policies exceeding one year, the NCD amount is given with respect to each claim-free policy year.",
        "Yes, expenses for health check-ups shall be reimbursed at the end of a block of two continuous policy years, provided the policy has been continuously renewed without a break. These expenses are subject to the limit stated in the Table of Benefits.",
        "The policy defines an AYUSH Hospital as a standalone or co-located facility registered with local authorities, supervised by a qualified AYUSH Medical Practitioner. It must have at least 5 in-patient beds, a qualified practitioner round the clock, dedicated therapy sections, and accessible daily patient records.",
        "AYUSH Treatment refers to medical and/or Hospitalisation treatments provided under Ayurveda, Yoga and Naturopathy, Unani, Siddha, and Homeopathy systems.",
        "Yes, room charges and intensive care unit charges per day for Plan A are payable up to the limit as shown in the Table of Benefits."
    ]
}
```

using pinecone db

```
{
    "answers": [
        "The grace period for payment of the premium shall be thirty days.",
        "The waiting period for pre-existing diseases to be covered is after the expiry of thirty six (36) months, provided they were declared at application and accepted.",
        "Yes, the policy covers maternity expenses. Conditions include: the female insured person must be continuously covered for 24 months, be between 18 and 45 years old, and limited to two deliveries/terminations. Exclusions apply, such as a 24-month waiting period (waivable for accident), more than one delivery per policy period, and ectopic pregnancy.",
        "The waiting period for cataract surgery is two years.",
        "Yes, the medical expenses incurred for an organ donor's hospitalization during the policy period for harvesting an organ donated to an insured person are covered, provided certain conditions are met, such as confirming to the Transplantation of Human Organs Act 1994.",
        "A No Claim Discount (NCD) of a flat 5% is allowed on the base premium upon renewal of policies with a term of one year, provided no claims were reported in the expiring policy. For policies exceeding one year, the aggregated NCD shall not exceed flat 5% of the total base premium for the term.",
        "Yes, expenses for health check-ups are reimbursed at the end of every two continuous policy years, provided the policy has been continuously renewed without a break. The reimbursement is subject to limits stated in the Table of Benefits, ranging from INR 5,000 to INR 10,000.",
        "A Hospital is an institution for in-patient and day care treatment of disease/injuries, registered with local authorities under the Clinical Establishments Act, 2010, OR meeting specific criteria. These criteria include qualified nursing/medical staff, minimum beds (10 or 15), a fully equipped operation theatre, and maintained patient records.",
        "The Company shall indemnify Medical Expenses incurred for Inpatient Care treatment under Ayurveda, Yoga and Naturopathy, Unani, Siddha and Homeopathy systems of medicines during each Policy Period up to the limit of Sum Insured as specified in the Policy Schedule in any AYUSH Hospital.",
        "Yes, for Plan A, room charges are limited to 1% of SI, max. INR 5,000 per day. ICU charges are limited to 2% of SI or actual, whichever is lower. These limits do not apply for listed procedures in a Preferred Provider Network as a package."
    ]
}
```
current issue--- response is tumba slow, 55secs per request



