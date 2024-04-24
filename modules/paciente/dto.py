from pydantic import BaseModel, Field
from datetime import datetime,time


class PacienteDTO(BaseModel):
    id: int 
    nome: str
    cpf: str = Field(..., min_length=11)
    sexo: str
    dt_nasc : datetime
    endereco: str
    bairro: str
    cidade: str
    estado : str
    contato: str
    id_login: int


    