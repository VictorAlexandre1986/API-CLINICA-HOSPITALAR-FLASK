from abc import ABC, abstractmethod

class PagamentoRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_pagamento(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_pagamentos(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_pagamento_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_pagamento(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_pagamento(self, id: int):
        raise Exception("Método não implementado")