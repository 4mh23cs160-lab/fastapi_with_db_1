from pydantic import BaseModel
from typing import Optional

class AIRequest(BaseModel):
    message: str
    system_prompt: str = "You are a helpful assistant."
    attachment_name: Optional[str] = None
    attachment_url: Optional[str] = None

class AIResponse(BaseModel):
    response: str
    attachment_name: Optional[str] = None
    attachment_url: Optional[str] = None