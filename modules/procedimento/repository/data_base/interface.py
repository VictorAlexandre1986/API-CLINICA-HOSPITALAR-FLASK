from abc import ABC, abstractmethod

class ProcedimentoRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_procedimento(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_procedimentos(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_procedimento_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_procedimento(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_procedimento(self, id: int):
        raise Exception("Método não implementado")