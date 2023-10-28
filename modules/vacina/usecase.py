from datetime import datetime

class VacinaUseCase:
    
    def __init__(self, vacina_repository):
        self.vacina_repository = vacina_repository
        
    
    def criar_vacina(self, id: int, nome: str, proposito:str, ml:float, estoque:int, vencimento:datetime):
        return self.vacina_repository.criar_vacina(id, nome, proposito, ml, estoque, vencimento)
    
    def buscar_vacina_por_id(self, id: int):
        return self.vacina_repository.buscar_vacina_por_id(id)
    
    def buscar_vacinas(self):
        return self.vacina_repository.buscar_vacinas()
    
    def deletar_vacina(self, id: int):
        return self.vacina_repository.deletar_vacina(id)
    
    def atualizar_vacina(self, id: int, nome: str, proposito:str, ml:float, estoque:int, vencimento:datetime):
        return self.vacina_repository.atualizar_vacina(id, nome, proposito, ml, estoque, vencimento)