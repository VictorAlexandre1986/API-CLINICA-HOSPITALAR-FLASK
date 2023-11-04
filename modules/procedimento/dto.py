from pydantic import BaseModel, Field
from datetime import datetime,time


class ProcedimentoDTO(BaseModel):
    id: int 
    procedimento: str
    preco: float
