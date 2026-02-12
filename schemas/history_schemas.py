from pydantic import BaseModel
from typing import List, Optional

class ChatHistorySchema(BaseModel):
    id: int
    user_id: int
    message: str
    response: str
    timestamp: str
    attachment_name: Optional[str] = None
    attachment_url: Optional[str] = None

    class Config:
        from_attributes = True

class ChatHistoryList(BaseModel):
    history: List[ChatHistorySchema]
