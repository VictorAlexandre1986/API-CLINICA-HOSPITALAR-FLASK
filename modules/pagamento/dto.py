from pydantic import BaseModel, Field
from datetime import datetime,time
from typing import List


class PagamentoDTO(BaseModel):
    id: int 
    id_paciente : int 
    data: datetime
    descricao_procedimentos: List[str] # Fazer uma busca pelos procedimentos e buscar os precos
    descricao_exames: List[str]
    descricao_vacinas: List[str]
    preco: float
    
class Pagamento_procedimentoDTO(BaseModel):
    preco : float | None
    nome: str | None
    descricao: str | None
    

class Pagamento_exameDTO(BaseModel):
    preco: float | None
    nome: str | None
    descricao: str | None


class Pagamento_vacinaDTO(BaseModel):
    preco: float | None   
    nome: str | None
    descricao : str | None