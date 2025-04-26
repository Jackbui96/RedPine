from fastapi import APIRouter
from models.schemas import QueryRequest, QueryResponse
from services.rag_engine import generate_response

router = APIRouter()

@router.post("/rag/query", response_model=QueryResponse)
async def query_handler(request: QueryRequest):
    return generate_response(request.query)
