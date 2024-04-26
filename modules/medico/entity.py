from pydantic import BaseModel
from datetime import datetime


class MedicoEntity(BaseModel):
    id: int 
    nome: str 
    crm: str
    especialidade: str
    contato: str
    id_login: int


