# PolicyRAG Latency Results

## Response Time Measurements

| Test Question | Response Time (seconds) |
|--------------|------------------------:|
| Annual Leave | 0.43 |
| Public Wi-Fi | 0.37 |
| Software Installation | 0.67 |
| Expense Claim | 0.39 |

---

## Performance Summary

| Metric | Value |
|--------|------:|
| Fastest Response | 0.37 seconds |
| Slowest Response | 0.67 seconds |
| Average Response | 0.47 seconds |
| Median (P50) | 0.41 seconds |
| Estimated P95 | 0.67 seconds |

---

## Performance Analysis

The introduction of caching for the embedding model, Chroma vector store, and Groq client significantly reduced response latency. Initial response times of approximately 11–17 seconds were reduced to less than one second for subsequent queries within the same Streamlit session. This optimization substantially improved the responsiveness and usability of the PolicyRAG application.

