# PolicyRAG Evaluation Questions

## Overview

The following questions were used to evaluate the retrieval quality, answer quality, citation accuracy, and response latency of the PolicyRAG system.

| Test No. | Question | Expected Policy |
|----------|----------|-----------------|
| 1 | How many annual leave days do employees receive? | Leave Policy |
| 2 | Can employees use public Wi-Fi? | Information Security Policy |
| 3 | Can I install software on my work laptop? | Acceptable Use Policy |
| 4 | How long do I have to submit an expense claim? | Expense Reimbursement Policy |
| 5 | What is considered a conflict of interest? | Code of Conduct |
| 6 | Can the company sell my personal information? | Data Privacy Policy |
| 7 | Is PPE mandatory? | Health and Safety Policy |
| 8 | Are meals reimbursed during business travel? | Business Travel Policy |
| 9 | Who should I report a phishing email to? | Information Security Policy |
| 10 | Do I need approval before travelling? | Business Travel Policy |

---

## Evaluation Objective

The objective of these evaluation questions is to verify that PolicyRAG can:

- Retrieve the correct policy document.
- Generate a grounded answer using retrieved context.
- Avoid hallucinations.
- Display correct citations.
- Respond with low latency.
