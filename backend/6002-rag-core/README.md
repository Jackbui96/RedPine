
# 6002-rag-core

This service powers the **Retrieval-Augmented Generation (RAG) Core** for the RedPine project, responsible for handling AI-driven query responses.

---

## 🚀 Overview

- **Technology**: FastAPI (Python)
- **Model**: Fine-tuned FLAN-T5
- **Running Port**: **6002**

This service:
- Accepts customer queries from the API Gateway
- Retrieves relevant context (documents)
- Generates AI-powered responses using the fine-tuned model

## 📦 Model Setup

- The fine-tuned FLAN-T5 model is **not stored inside the container**.
- **First-time setup**: Download the model manually from [Google Drive](https://drive.google.com/drive/folders/1i-oqb0i18298fQNO9wyJW0mjNSkIU-kJ?usp=sharing).
- Place the downloaded model files into the `finetune-hf/models/` directory before starting the service.

## 🔧 Setup Instructions

1. Navigate to the service directory:

```bash

cd backend/6002-rag-core
```

2. Install dependencies:

```bash

pip install -r requirements.txt
```

3. Run the RAG Core service locally:

```bash

python text2text-generation.py
```

## 🌍 Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| MODEL_DIR | Path to local model files | `./finetune-hf/models/customer-support-llm/` |

Example `.env`:

```bash

MODEL_DIR=./finetune-hf/models/customer-support-llm/
```

## 🌍 API Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/rag/query` | Accepts a customer query and returns an AI-generated response |

## 🛠️ Notes

- Model is loaded once at startup to optimize inference speed.
- Designed to be memory-efficient and fast for real-time queries.

---

> 📘 The RAG Core ensures low-latency, context-aware, dynamic customer interactions for RedPine platform.
