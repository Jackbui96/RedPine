from fastapi import APIRouter, Depends, UploadFile, File
from models.schemas import QueryRequest, FeedbackRequest, QueryResponse
# from app.core.rag_engine import generate_response
# from app.services.upload import process_document
# from app.services.feedback import save_feedback

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_handler(request: QueryRequest):
    return generate_response(request.query)

@router.post("/upload")
async def upload_handler(file: UploadFile = File(...)):
    return await process_document(file)

@router.post("/feedback")
async def feedback_handler(feedback: FeedbackRequest):
    return save_feedback(feedback)
