from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email:str
    is_active: bool
    
class UserOut(UserBase):
    id: int
    created_at: datetime 

    class Config:
        orm_mode = True 