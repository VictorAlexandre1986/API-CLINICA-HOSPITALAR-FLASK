from pydantic import BaseModel
from datetime import datetime


class MedicoDTO(BaseModel):
    id: int 
    nome: str 
    crm: str
    especialidade: str
    contato: str
    contato2: str
    sexo: str
    endereco: str
    num: str
    bairro: str
    cidade: str
