from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from repositories.history_repo import HistoryRepo
from schemas.history_schemas import ChatHistorySchema, ChatHistoryList
from utils.jwt_handler import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/history", tags=["history"])
security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = verify_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload.get("sub") # Assuming sub is user_id

@router.get("/", response_model=ChatHistoryList)
def get_history(
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    repo = HistoryRepo(db)
    history = repo.get_user_history(user_id)
    return {"history": history}
