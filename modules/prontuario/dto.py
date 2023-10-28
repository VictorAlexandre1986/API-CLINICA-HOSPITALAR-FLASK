from pydantic import BaseModel, Field
from datetime import datetime,time


class ProntuarioDTO(BaseModel):
    id: int 
    cpf: str = Field(..., min_length=11)
    procedimento: int
    vacina: int
    