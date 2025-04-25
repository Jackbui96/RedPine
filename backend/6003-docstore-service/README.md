
# 6003-docstore-service

This service handles the **document storage, retrieval, and S3 integration** for the RedPine project.

---

## 🚀 Overview

- **Technology**: FastAPI (Python)
- **Storage Backend**: AWS S3 (or compatible storage)
- **Running Port**: **6003**

This service:
- Allows users to upload documents
- Stores document files securely in AWS S3
- Lists and retrieves documents for downstream services (like RAG Core)

## 🔧 Setup Instructions

1. Navigate to the service directory:

```bash

cd backend/6003-docstore-service
```

2. Install dependencies:

```bash

pip install -r requirements.txt
```

3. Run the Docstore service locally:

```bash

uvicorn main:app --reload --port 6003
```

## 🔐 Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| AWS_ACCESS_KEY_ID | AWS Access Key for S3 | `AKIA...` |
| AWS_SECRET_ACCESS_KEY | AWS Secret Key for S3 | `abcd1234...` |
| S3_BUCKET_NAME | Target S3 bucket name | `redpine-docstore` |
| S3_REGION | AWS region | `us-west-2` |

Example `.env` file:

```bash

AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
S3_BUCKET_NAME=your-bucket-name
S3_REGION=your-region
```

## 🌍 API Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/docstore/upload` | Upload a document to S3 |
| GET  | `/api/docstore/list` | List all documents available in the S3 bucket |

## 🛠️ Notes

- Uploads are automatically validated (size, type) before being pushed to S3.
- Documents are stored in a clean, organized structure inside the bucket.
- Designed for high-availability and easy expansion (e.g., adding metadata indexing later).

---

> 📘 The Docstore service ensures reliable document management for all AI and user-facing modules of RedPine.
