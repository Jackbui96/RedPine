from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    response: str

class FeedbackRequest(BaseModel):
    query_id: int
    rating: int
    comment: str = ""
