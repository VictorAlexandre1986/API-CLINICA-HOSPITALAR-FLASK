from pydantic import BaseModel, Field
from datetime import datetime,time


class PagamentoDTO(BaseModel):
    id: int 
    id_paciente : int 
    procedimento: str # Fazer uma busca pelos procedimentos e buscar os precos
    exame: str
    vacina: str
    preco_total: float