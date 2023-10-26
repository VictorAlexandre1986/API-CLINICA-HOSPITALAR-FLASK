from pydantic import BaseModel, Field
from datetime import datetime,time


class AgendaEntity(BaseModel):
    id: int 
    cpf: str = Field(..., min_length=11)
    dia: datetime
    hora: time
    procedimento: str
    medico: str 
    date_create : datetime
    update_create: datetime