import os
import grpc
from transformers import pipeline
from models.schemas import QueryResponse
from protos import model_transfer_pb2, model_transfer_pb2_grpc

# gRPC config
DOCSTORE_SERVICE_ADDR = "docstore:6003"

MODEL_DIR = "/tmp/customer-support-llm"

def fetch_model_via_grpc():
    channel = grpc.insecure_channel(DOCSTORE_SERVICE_ADDR)
    stub = model_transfer_pb2_grpc.ModelTransferServiceStub(channel)

    print(f"🚀 Requesting model download via gRPC to docstore {DOCSTORE_SERVICE_ADDR}...")
    request = model_transfer_pb2.ModelPayload(model_folder="customer-support-llm")
    response = stub.SendModel(request)

    if not response.success:
        raise RuntimeError(f"❌ Failed to download model: {response.message}")
    print(f"✅ Model downloaded: {response.message}")

if not os.path.exists(MODEL_DIR):
    fetch_model_via_grpc()

print(f"📦 Loading model from {MODEL_DIR}...")
pipe = pipeline(
    "text2text-generation",
    model=MODEL_DIR,
    tokenizer=MODEL_DIR
)

def generate_response(query) -> QueryResponse:
    output = pipe(query, max_length=100, do_sample=False)
    return QueryResponse(
        response=output[0]["generated_text"]
    )
