# Agentic-IT-Desk-AI-Helpdesk-Agent

# Agentic IT Desk – AI Helpdesk Agent

An AI-powered IT Helpdesk Assistant built using **Agentic RAG, LangGraph, FastAPI, Pinecone, and Large Language Models (LLMs)**. The system helps users resolve IT-related queries by retrieving information from a private knowledge base, evaluating retrieved information, and using web search when internal documentation is insufficient.

## Project Overview

Traditional IT helpdesks often receive repetitive support requests related to:

- Password and account issues
- VPN connectivity
- Software installation and configuration
- Network and system troubleshooting
- Access and authentication problems
- Common IT policies and procedures

Finding the correct solution manually can be time-consuming. A traditional chatbot may also generate answers without checking whether the information is reliable.

This project addresses these problems through an **Agentic Retrieval-Augmented Generation (RAG)** workflow.

The agent retrieves relevant information, evaluates its quality, decides whether additional retrieval is needed, and generates an answer based on available evidence.

## Key Features

- **Agentic RAG Workflow:** Uses LangGraph to manage the complete question-answering process.
- **Private Knowledge Retrieval:** Retrieves relevant information from the Pinecone vector database.
- **Evidence Grading:** Evaluates whether retrieved documents are relevant to the user's question.
- **Intelligent Query Routing:** Routes greetings and general queries separately from IT support questions.
- **Web Search Fallback:** Uses Tavily when internal knowledge is insufficient.
- **Query Rewriting:** Improves weak search queries and retries retrieval when required.
- **Grounded Responses:** Generates answers using retrieved information and avoids answering unsupported questions as if they were facts.
- **Document Ingestion:** Allows authorized administrators to upload knowledge-base documents.
- **REST API:** Provides backend endpoints through FastAPI.
- **Audit Logging:** Records query and workflow information for monitoring and debugging.
- **Web Interface:** Provides a simple interface for interacting with the IT support agent.

## System Architecture

```text
                 User
                  |
                  v
           Web Interface
          (HTML/CSS/JS)
                  |
                  v
               FastAPI
                  |
                  v
             LangGraph
           Agentic Workflow
                  |
                  v
           Question Routing
                  |
          +-------+-------+
          |               |
          v               v
     IT Support       General Query
          |
          v
    Pinecone Retrieval
          |
          v
     Evidence Grading
          |
      +---+---+
      |       |
     Good    Weak
      |       |
      v       v
   Generate  Tavily Search
   Answer       |
                v
          Evidence Grading
                |
                v
          Query Rewriting
          (if necessary)
                |
                v
          Generate Answer
```

## Agentic RAG Workflow

The system follows a conditional workflow rather than simply retrieving documents and generating an answer.

1. **Question Routing:** Determines whether the incoming question requires IT knowledge retrieval or a direct response.
2. **Private Knowledge Retrieval:** Searches the Pinecone knowledge base for relevant documents.
3. **Evidence Grading:** Evaluates whether the retrieved information is sufficient and relevant.
4. **Web Search:** Uses Tavily when the private knowledge base does not provide sufficient evidence.
5. **Web Evidence Grading:** Evaluates the relevance of external search results.
6. **Query Rewriting:** Rephrases weak queries to improve retrieval.
7. **Answer Generation:** Generates a response using the available supporting information.
8. **Insufficient Evidence:** Avoids presenting unsupported information as a confirmed solution.

## Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Backend | Python, FastAPI | REST API and application logic |
| Agent Framework | LangGraph | Workflow orchestration and conditional routing |
| LLM | OpenAI | Language understanding and response generation |
| Embeddings | OpenAI Embeddings | Converts text into vector representations |
| Vector Database | Pinecone | Stores and retrieves knowledge-base embeddings |
| Web Search | Tavily | External information retrieval |
| Frontend | HTML, CSS, JavaScript | User interface |
| Database | SQLite | Audit logging |
| Package Manager | uv | Python dependency and environment management |

## Project Structure

```text
Agentic-IT-Desk-AI-Helpdesk-Agent/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── rag/
│   │   ├── state.py
│   │   ├── vectorstore.py
│   │   └── workflow.py
│   │
│   ├── services/
│   │   ├── audit.py
│   │   └── ingestion.py
│   │
│   └── main.py
│
├── data/
│   └── sample_kb/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── templates/
│   └── index.html
│
├── tests/
│
├── uploads/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── ingest_sample_kb.py
├── pyproject.toml
├── run.py
└── README.md
```

## Getting Started

### Prerequisites

Make sure you have installed:

- Python 3.12 or a compatible version
- uv package manager
- Pinecone account
- OpenAI API key
- Tavily API key

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Agentic-IT-Desk-AI-Helpdesk-Agent
```

### 2. Create and Activate the Virtual Environment

```bash
uv venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

If your project dependencies are configured in `pyproject.toml`:

```bash
uv sync
```

Alternatively, if you are using `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
# Application
APP_ENV=development

# OpenAI
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small

# Tavily
TAVILY_API_KEY=your_tavily_api_key

# Pinecone
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=agentic-it-desk
PINECONE_NAMESPACE=agentic-it-desk

# Security
ADMIN_API_KEY=your_secure_admin_key
```

**Important:** Use the exact environment variable names and model settings expected by your application configuration. Never upload your actual `.env` file or API keys to GitHub.

### 5. Configure Pinecone

1. Create a Pinecone account.
2. Create an index with the dimensions and similarity metric required by your embedding model.
3. Configure the index name and namespace in your `.env` file.
4. Make sure the API key belongs to the same Pinecone project as the index.

For `text-embedding-3-small`, use **1536 dimensions**.

### 6. Ingest Knowledge-Base Documents

Run:

```bash
uv run python ingest_sample_kb.py
```

The ingestion pipeline processes documents, splits them into chunks, generates embeddings, and stores the vectors in Pinecone.

Supported document formats depend on the ingestion implementation and include PDF, TXT, Markdown, and DOCX.

### 7. Run the Application

```bash
uv run python run.py
```

Open the application:

**http://127.0.0.1:8080**

FastAPI Swagger documentation:

**http://127.0.0.1:8080/docs**

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Opens the web interface |
| GET | `/api/health` | Checks application health |
| POST | `/api/chat` | Sends a question to the AI agent |
| POST | `/api/ingest` | Uploads a knowledge-base document |

The document ingestion endpoint requires the configured admin key in the `X-Admin-Key` request header.

## Example Use Cases

### 1. VPN Troubleshooting

**Question:**

"How can I connect to the company VPN?"

**Expected workflow:**

```text
Question
   |
   v
Question Router
   |
   v
Private Knowledge Retrieval
   |
   v
Evidence Grading
   |
   v
Generate Answer
```

### 2. Password and MFA Support

**Question:**

"What should I do if I cannot access my account?"

The agent searches the internal knowledge base for account recovery and authentication instructions before generating a response.

### 3. Current IT Information

**Question:**

"Is there a current outage affecting Microsoft Teams?"

If the internal knowledge base does not contain sufficient information, the agent can use Tavily to retrieve relevant external information.

### 4. Query Rewriting

**Question:**

"My application stopped working after an update. What should I do?"

If the initial retrieval is insufficient, the agent can rewrite the query and retry retrieval.

## Security Considerations

- Store API keys in environment variables.
- Never commit `.env` files to GitHub.
- Protect document ingestion endpoints using an admin key.
- Validate uploaded documents before processing.
- Avoid exposing internal knowledge-base content to unauthorized users.
- Configure appropriate API access and usage limits.

## Future Improvements

- Docker-based deployment.
- User authentication and role-based access control.
- Integration with ticketing systems.
- More advanced monitoring and observability.
- Improved document metadata and source citations.
- Automated knowledge-base updates.
- Production deployment with scalable infrastructure.

## Learning Outcomes

This project demonstrates practical implementation of:

- Agentic AI and Retrieval-Augmented Generation
- LangGraph state management and conditional workflows
- Vector search and semantic retrieval
- Document processing and embedding generation
- LLM integration with external tools
- FastAPI backend development
- REST API integration with a frontend
- Environment configuration and API security
- AI application debugging and deployment fundamentals

---

**Project:** Agentic IT Desk – AI Helpdesk Agent  
**Category:** Agentic AI / RAG / IT Automation  
**Status:** Development