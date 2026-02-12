from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from db import get_db
from utils.ai_response import get_completion
from schemas.ai_response_schemas import AIRequest, AIResponse
from repositories.history_repo import HistoryRepo
from utils.jwt_handler import verify_token
from typing import Optional

router = APIRouter()

@router.post("/ask", response_model=AIResponse)
def ask_ai(
    request: AIRequest, 
    db: Session = Depends(get_db),
    Authorization: Optional[str] = Header(None)
):
    """Get response from AI model and optionally save to history."""
    try:
        response = get_completion(request.message, request.system_prompt)
        
        # Save to history if user is logged in
        if Authorization:
            try:
                token = Authorization.split(" ")[1] if " " in Authorization else Authorization
                payload = verify_token(token)
                if payload:
                    user_id = int(payload.get("sub"))
                    history_repo = HistoryRepo(db)
                    history_repo.save_chat(
                        user_id, 
                        request.message, 
                        response,
                        attachment_name=request.attachment_name,
                        attachment_url=request.attachment_url
                    )
            except Exception as e:
                print(f"Failed to save history: {e}")

        return AIResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    