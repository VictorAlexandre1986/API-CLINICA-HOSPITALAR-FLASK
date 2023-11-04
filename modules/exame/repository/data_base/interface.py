from abc import ABC, abstractmethod

class ExameRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_exame(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_exames(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_exame_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_exame(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_exame(self, id: int):
        raise Exception("Método não implementado")