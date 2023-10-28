from abc import ABC, abstractmethod

class PacienteRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_paciente(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_pacientes(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_paciente_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_paciente(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_paciente(self, id: int):
        raise Exception("Método não implementado")