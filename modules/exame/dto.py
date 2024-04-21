from pydantic import BaseModel, Field
from datetime import datetime,time

class ExameDTO(BaseModel):
    id: int 
    tipo_exame: str = Field(..., min_length=3)
    valor: float = Field(..., gt=50.0)  # Definindo o valor mínimo como 50.0