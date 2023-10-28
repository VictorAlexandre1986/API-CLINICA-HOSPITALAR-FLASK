from pydantic import BaseModel
from datetime import datetime


class VacinaDTO(BaseModel):
    id: int 
    nome: str
    proposito: str
    ml: float
    estoque: int
    vencimento: datetime
