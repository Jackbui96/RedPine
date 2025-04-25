
# RedPine RAG Core Service

[![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-green)](https://fastapi.tiangolo.com/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Transformers-orange)](https://huggingface.co/docs/transformers/index)
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

---

## 💡 Project Introduction

**RedPine** is an intelligent customer support platform composed of two major components:

* **Backend**: Where core business logic, document management, and the fine-tuned FLAN-T5 model are built and served through microservices.

* **Frontend**: A simple React + Vite web interface providing a user-friendly chat interaction with the RAG Core Service.

The **RAG Core Service** specifically utilizes **Retrieval-Augmented Generation (RAG)** principles to combine the strengths of information retrieval and large language model (LLM) generation.

This service enhances traditional AI chatbot capabilities by ensuring:

* Faster and more accurate responses

* Contextually grounded answers based on real company documents

* Reduced hallucination and misinformation from the model

Built with **FastAPI** and a fine-tuned **FLAN-T5 model**, it seamlessly integrates with the RedPine API Gateway and Docstore services.

---

## 🔗 How It Works

1. **User Query Input:**
    - A customer sends a question to the API Gateway frontend.

2. **Retrieval Phase:**
    - Relevant document chunks are retrieved from the Docstore's indexed knowledge base (future roadmap).

3. **Generation Phase:**
    - The fine-tuned FLAN-T5 model generates a customized, context-aware response.

4. **Response Delivery:**
    - The API Gateway delivers the generated answer back to the frontend client.

---

## 📊 Core Technologies

- **FastAPI** for building a lightweight, high-performance API.
- **Hugging Face Transformers** for hosting the fine-tuned FLAN-T5 model.
- **Datasets** and **Sentence Transformers** for future retrieval integration.
- **AWS S3** for document storage (via Docstore Service).
- **Google Drive** to hold downloadable model artifacts and training data.

---

## 🚀 Key Features

- Fine-tuned model specifically for customer support and order management domains
- API ready for integration into React/Vite frontend applications
- Lightweight, Docker-ready, and cloud-deployable
- Future extensibility for Retrieval + Generation combined workflows

---

> 📘 The RedPine RAG Core Service bridges the gap between static FAQs and dynamic, personalized AI-driven customer support.
