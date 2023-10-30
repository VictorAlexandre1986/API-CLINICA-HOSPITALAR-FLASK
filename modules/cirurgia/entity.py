from pydantic import BaseModel, Field
from datetime import datetime,time


class CirurgiaEntity(BaseModel):
    id: int 
    nome_cirurgia: str