from pydantic import BaseModel, Field
from datetime import datetime,time

class ExameDTO(BaseModel):
    id: int 
    exame: str
    preco: float