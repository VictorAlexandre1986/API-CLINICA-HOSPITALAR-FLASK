from pydantic import BaseModel, Field
from datetime import datetime,time


class AgendaEntity(BaseModel):
    id: int 
    cpf: str = Field(..., min_length=11)
    dia: datetime
    id_procedimento: int | None
    id_medico: int | None
    id_cirurgia : int | None