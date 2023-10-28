from abc import ABC, abstractmethod

class ProntuarioRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_prontuario(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_prontuarios(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_prontuario_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_prontuario(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_prontuario(self, id: int):
        raise Exception("Método não implementado")