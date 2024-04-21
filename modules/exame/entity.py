from pydantic import BaseModel, Field
from datetime import datetime,time

class ExameEntity(BaseModel):
    id: int 
    tipo_exame: str 
    valor: float  