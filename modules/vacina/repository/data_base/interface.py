from abc import ABC, abstractmethod

class VacinaRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_vacina(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_vacinas(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_vacina_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_vacina(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_vacina(self, id: int):
        raise Exception("Método não implementado")