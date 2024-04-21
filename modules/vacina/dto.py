from pydantic import BaseModel
from datetime import datetime


class VacinaDTO(BaseModel):
    id: int | None
    nome: str
    proposito: str
    ml: float
    estoque: int
    vencimento: datetime
