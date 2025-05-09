from fastapi import APIRouter, HTTPException
from app.models import QueryRequest, QueryResponse
from app.services.vector_service import VectorService
from app.services.llm_service import LLMService

router = APIRouter()
vector_service = VectorService()
llm_service = LLMService()

@router.post("/ask", response_model=QueryResponse)
async def ask_question(req: QueryRequest):
    try:
        # Get context from vector search
        context = vector_service.get_context(req.query)
        
        if not context.strip():
            return QueryResponse(
                query=req.query,
                answer="I couldn't find any relevant information for your question."
            )

        # Generate response using LLM
        answer = llm_service.generate_response(req.query, context)
        
        return QueryResponse(
            query=req.query,
            answer=answer
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 