from datetime import datetime, time

class ExameUseCase:
    
    def __init__(self, exame_repository):
        self.exame_repository = exame_repository
        
    
    def criar_exame(self, id: int,exame: str, preco: float):
        return self.exame_repository.criar_exame(id, exame, preco)
    
    def buscar_exame_por_id(self, id: int):
        return self.exame_repository.buscar_exame_por_id(id)
    
    def buscar_exames(self):
        return self.exame_repository.buscar_exames()
    
    def deletar_exame(self, id: int):
        return self.exame_repository.deletar_exame(id)
    
    def atualizar_exame(self, id: int, exame: str, preco: float):
        return self.exame_repository.atualizar_exame(id, exame, preco)