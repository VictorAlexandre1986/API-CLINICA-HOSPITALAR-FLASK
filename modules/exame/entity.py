from pydantic import BaseModel, Field
from datetime import datetime,time

class ExameEntity(BaseModel):
    id: int 
    exame: str
    preco: float