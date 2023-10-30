from abc import ABC, abstractmethod

class AuxiliarRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_auxiliar(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_auxiliars(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_auxiliar_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_auxiliar(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_auxiliar(self, id: int):
        raise Exception("Método não implementado")