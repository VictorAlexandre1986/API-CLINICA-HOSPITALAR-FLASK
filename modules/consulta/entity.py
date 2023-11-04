from pydantic import BaseModel, Field
from datetime import datetime,time


class ConsultaEntity(BaseModel):
    id: int 
    data: datetime
    hora: time
    procedimento: str | None
    exame: str | None
    vacina: str | None
    medico: str | None
    auxiliar: str | None