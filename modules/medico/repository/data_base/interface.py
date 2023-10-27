from abc import ABC, abstractmethod

class MedicoRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_medico(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_medicos(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_medico_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_medico(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_medico(self, id: int):
        raise Exception("Método não implementado")