from pydantic import BaseModel, Field
from datetime import datetime,time


class LoginEntity(BaseModel):
    id: int 
    usuario: str = Field(..., min_length=3)
    senha: str = Field(..., min_length=3)