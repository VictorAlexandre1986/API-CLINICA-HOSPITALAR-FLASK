from abc import ABC, abstractmethod

class ConsultaRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_consulta(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_consultas(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_consulta_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_consulta(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_consulta(self, id: int):
        raise Exception("Método não implementado")