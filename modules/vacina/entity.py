from pydantic import BaseModel
from datetime import datetime


class EntityDTO(BaseModel):
    id: int 
    nome: str
    proposito: str
    ml: float
    estoque: int
    vencimento: datetime