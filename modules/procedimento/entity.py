from pydantic import BaseModel, Field
from datetime import datetime,time


class ProcedimentoDTO(BaseModel):
    id: int 
    data: datetime
    hora: time
    procedimento: str
    medico: str 
    auxiliar: str