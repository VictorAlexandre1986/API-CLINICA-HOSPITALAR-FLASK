from abc import ABC, abstractmethod

class CirurgiaRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_cirurgia(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_cirurgias(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_cirurgia_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_cirurgia(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_cirurgia(self, id: int):
        raise Exception("Método não implementado")