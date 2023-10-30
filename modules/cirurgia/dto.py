from pydantic import BaseModel, Field
from datetime import datetime,time


class CirurgiaDTO(BaseModel):
    id: int 
    nome_cirurgia: str

    