from sqlalchemy.orm import Session
from models import ChatHistory
from datetime import datetime

class HistoryRepo:
    def __init__(self, db: Session):
        self.db = db

    def save_chat(self, user_id: int, message: str, response: str, attachment_name: str = None, attachment_url: str = None):
        db_chat = ChatHistory(
            user_id=user_id,
            message=message,
            response=response,
            timestamp=datetime.now().isoformat(),
            attachment_name=attachment_name,
            attachment_url=attachment_url
        )
        self.db.add(db_chat)
        self.db.commit()
        self.db.refresh(db_chat)
        return db_chat

    def get_user_history(self, user_id: int, limit: int = 50):
        return self.db.query(ChatHistory).filter(ChatHistory.user_id == user_id).order_by(ChatHistory.id.desc()).limit(limit).all()
