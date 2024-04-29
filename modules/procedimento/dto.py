from pydantic import BaseModel, Field
from datetime import datetime,time


class ProcedimentoDTO(BaseModel):
    id: int 
    procedimento: str
    id_exame: int | None
    id_vacina: int | None
    id_cirurgia: int | None
    id_medico: int | None
    id_paciente: int | None
    id_auxiliar: int | None
