from pydantic import BaseModel, Field
from datetime import datetime,time


class ProcedimentoEntity(BaseModel):
    id: int 
    procedimento: str
    preco: float