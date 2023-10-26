from pydantic import BaseModel, Field
from datetime import datetime,time


class LoginEntity(BaseModel):
    id: int 
    usuario: str = Field(..., min_length=11)
    senha: str = Field(..., min_length=8)
    update_create: datetime | None