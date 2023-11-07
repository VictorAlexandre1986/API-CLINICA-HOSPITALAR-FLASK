from pydantic import BaseModel, Field
from datetime import datetime,time
from typing import List

class PagamentoEntity(BaseModel):
    id: int 
    id_paciente : int 
    data: datetime
    descricao_procedimentos: List[str] # Fazer uma busca pelos procedimentos e buscar os precos
    descricao_exames: List[str]
    descricao_vacinas: List[str]
    preco: float