from pydantic import BaseModel, Field
from datetime import datetime,time


class PacienteEntity(BaseModel):
    id: int 
    nome: str
    cpf: str = Field(..., min_length=11)
    sexo: str
    endereco: str
    num: str
    bairro: str
    cidade: str
    contato: str
    contato2: str
    email: str