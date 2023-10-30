from pydantic import BaseModel, Field
from datetime import datetime,time


class AuxiliarEntity(BaseModel):
    id: int 
    nome: str
    cpf: str = Field(..., min_length=11)
    endereco: str
    num: str
    cidade: str
    contato: str
    contato2: str
    coren: str