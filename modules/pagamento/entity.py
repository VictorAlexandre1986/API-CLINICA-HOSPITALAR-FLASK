from pydantic import BaseModel, Field
from datetime import datetime,time

class PagamentoEntity(BaseModel):
    id: int 
    id_paciente : int 
    data: datetime
    procedimento: str # Fazer uma busca pelos procedimentos e buscar os precos
    exame: str
    vacina: str
    valor_total: float