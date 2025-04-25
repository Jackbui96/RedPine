
# RedPine Backend

This is the backend system for the **RedPine** project. It consists of multiple microservices focused on handling AI-driven customer support and document retrieval.

---

## 🗂️ Backend Structure

```plaintext
backend/
├── 6001-api-gateway/       # FastAPI Gateway for routing external API requests (port 6001)
├── 6002-rag-core/          # FastAPI RAG Core Service for LLM query handling (port 6002)
├── 6003-docstore-service/  # FastAPI Docstore Service for document upload/download to S3 (port 6003)
```

Each service is containerized and runs independently.

## 🚀 Service Details

### 6001-api-gateway (Port 6001)
- Acts as a central API gateway for frontend applications.
- Handles routing, CORS policies, authentication (optional).
- Proxies requests to internal microservices (`rag-core`, `docstore`).

### 6002-rag-core (Port 6002)
- Retrieval-Augmented Generation (RAG) Core Service.
- Fine-tuned FLAN-T5 model that handles customer queries.
- Exposes an API for query input and returns AI-generated responses.
- **First-time setup:** Download the model files from [Google Drive](https://drive.google.com/drive/folders/1i-oqb0i18298fQNO9wyJW0mjNSkIU-kJ?usp=sharing) and place them into the `finetune-hf/models/` directory.

### 6003-docstore-service (Port 6003)
- Manages document ingestion, retrieval, and storage.
- **Connects securely to AWS S3** to upload and download document files.
- Handles file chunking, embedding, and indexing if needed.

## 📂 Model and Dataset Sources

- ✨ **Trained Model:**
    - Stored in a secured **Google Drive folder**.
    - On service startup, `6002-rag-core` downloads model artifacts (e.g., `model.safetensors`, `tokenizer.json`).

- 📚 **Original Training CSV:**
    - Also located in the shared **Google Drive**.
    - Contains original `instruction` and `response` pairs for reference or retraining.

## 🔐 Secrets Management

- AWS credentials for **S3 access** are handled securely using environment variables or IAM roles.
- Google Drive access (if using APIs) should also be secured via `.env` configurations or service accounts.

## 📦 Deployment Notes

- All services are Docker-ready.
- For production deployment, use an orchestrator like Kubernetes or Docker Compose.
- HTTPS Termination and Load Balancing recommended via NGINX or AWS ALB.

---

## 📅 Quick Start (Local)

```bash
# Start API Gateway
cd 6001-api-gateway
uvicorn main:app --reload --port 6001

# Start RAG Core
cd 6002-rag-core
uvicorn main:app --reload --port 6002

# Start Docstore
cd 6003-docstore-service
uvicorn main:app --reload --port 6003
```

## 🌍 Environment Variables Required

| Variable | Purpose |
|----------|---------|
| AWS_ACCESS_KEY_ID | S3 bucket access |
| AWS_SECRET_ACCESS_KEY | S3 bucket access |
| S3_BUCKET_NAME | Target S3 bucket |
| GOOGLE_DRIVE_MODEL_ID | GDrive Model file ID |
| GOOGLE_DRIVE_CSV_ID | GDrive CSV file ID |

---

> 📅 Designed with scalability and modularity in mind. Each microservice is independently maintainable and replaceable.
