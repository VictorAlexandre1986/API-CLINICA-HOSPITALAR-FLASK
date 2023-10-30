from datetime import datetime,time

class CirurgiaUseCase:
    
    def __init__(self, cirurgia_repository):
        self.cirurgia_repository = cirurgia_repository
        
    
    def criar_cirurgia(self, id: int, nome_cirurgia: str):
        return self.cirurgia_repository.criar_cirurgia(id, nome_cirurgia)
    
    def buscar_cirurgia_por_id(self, id: int):
        return self.cirurgia_repository.buscar_cirurgia_por_id(id)
    
    def buscar_cirurgias(self):
        return self.cirurgia_repository.buscar_cirurgias()
    
    def deletar_cirurgia(self, id: int):
        return self.cirurgia_repository.deletar_cirurgia(id)
    
    def atualizar_cirurgia(self, id: int, nome_cirurgia):
        return self.cirurgia_repository.atualizar_cirurgia(id, nome_cirurgia)