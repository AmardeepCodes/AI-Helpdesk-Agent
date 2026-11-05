# Synthetic RAG Company Dataset

All company names, people, employee IDs, assets, policies, and contact addresses in this dataset are fictional.
The `.example` email domain is reserved for examples.

## Contents
- `documents/`: 11 Markdown knowledge-base documents for chunking and embedding.
- `employees.csv`: synthetic employee directory for structured retrieval tests.
- `assets.csv`: synthetic device inventory.
- `rag_test_queries.json`: sample questions, expected answers, and source-document hints.

## Suggested ingestion
1. Ingest each Markdown file separately.
2. Preserve `Document ID`, `Department`, `Last updated`, and `Classification` as metadata where possible.
3. Chunk by headings or paragraphs; avoid splitting question/answer pairs.
4. Add `source` metadata with the relative filename.
5. Keep CSV data in a separate namespace or convert each row to a small document with employee/asset metadata.

## Suggested RAG evaluation
- Retrieval test: does the top-k result include the expected source?
- Grounding test: does the answer match the expected answer?
- Abstention test: for questions not covered by the corpus, does the assistant say the information is unavailable?
- Metadata test: filter by department or classification.
- Multi-hop test: ask for an employee's device and office using `employees.csv` plus `assets.csv`.

## Example questions not answered by this corpus
- Who is the CEO?
- What is the company's annual revenue?
- What is the office Wi-Fi password?
- What is the exact home internet reimbursement amount?

The correct behavior for these is to abstain rather than fabricate.
