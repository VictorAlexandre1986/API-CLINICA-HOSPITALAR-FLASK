from abc import ABC, abstractmethod

class AgendaRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_agenda(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_agendas(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_agenda_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_agenda(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_agenda(self, id: int):
        raise Exception("Método não implementado")