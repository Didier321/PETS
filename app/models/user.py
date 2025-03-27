from sqlalchemy import String, Integer, Column, Boolean, TIMESTAMP, text
from app.core.database import Base





class User(Base):
    __tablename__ = 'user'
    id= Column(Integer, primary_key=True)
    name=Column(String(60), nullable=False)
    email= Column(String(80), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
