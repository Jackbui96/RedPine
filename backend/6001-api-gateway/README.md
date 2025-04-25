
# 6001-api-gateway

This service acts as the **central API Gateway** for the RedPine project, providing a single point of entry for routing client requests to internal microservices.

---

## 🚀 Overview

- **Technology**: FastAPI (Python)
- **Purpose**: Route requests to internal services (RAG Core and Docstore)
- **Running Port**: **6001**

This service helps:
- Apply CORS policies
- Authenticate incoming requests (optional/future)
- Proxy and load-balance traffic to downstream services
- Provide a unified API surface for frontend applications

## 📦 Service Connections

| Service | Purpose | URL Mapping |
|---------|---------|-------------|
| 6002-rag-core | Handles AI query processing | `/api/rag/` |
| 6003-docstore-service | Manages documents, S3 integration | `/api/docstore/` |

All incoming routes are prefixed and forwarded appropriately.

## 🔧 Setup Instructions

1. Navigate to the service directory:

```bash

cd backend/6001-api-gateway
```

2. Install dependencies:

```bash

pip install -r requirements.txt
```

3. Run the API Gateway locally:

```bash

uvicorn main:app --reload --port 6001
```

## 🌍 Environment Variables

You can configure service addresses via environment variables (optional):

| Variable | Purpose | Default |
|----------|---------|---------|
| RAG_CORE_URL | Base URL of RAG Core service | `http://localhost:6002` |
| DOCSTORE_URL | Base URL of Docstore service | `http://localhost:6003` |

Create a `.env` file if you want to override defaults:

```bash

RAG_CORE_URL=http://localhost:6002
DOCSTORE_URL=http://localhost:6003
```

## 🌍 API Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/rag/query` | Send a customer query to RAG Core |
| POST | `/api/docstore/upload` | Upload documents to Docstore |
| GET  | `/api/docstore/list` | List available documents |

## 🛠️ Notes

- Handles CORS by default for frontend on ports 3000/3001 (React apps)
- Authentication, rate limiting, and API key management are **planned for future upgrades**.

---

> 📘 Designed to keep services modular, secure, and scalable in RedPine project architecture.
