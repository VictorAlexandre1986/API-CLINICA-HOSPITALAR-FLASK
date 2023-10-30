from datetime import datetime,time

class AuxiliarUseCase:
    
    def __init__(self, auxiliar_repository):
        self.auxiliar_repository = auxiliar_repository
        
    
    def criar_auxiliar(self, id: int, cpf: str, procedimento: int, vacina: int):
        return self.auxiliar_repository.criar_auxiliar(id, cpf, procedimento, vacina)
    
    def buscar_auxiliar_por_id(self, id: int):
        return self.auxiliar_repository.buscar_auxiliar_por_id(id)
    
    def buscar_auxiliars(self):
        return self.auxiliar_repository.buscar_auxiliars()
    
    def deletar_auxiliar(self, id: int):
        return self.auxiliar_repository.deletar_auxiliar(id)
    
    def atualizar_auxiliar(self,id:int, cpf: str, procedimento:str, vacina: int):
        return self.auxiliar_repository.atualizar_auxiliar(id, cpf, procedimento, vacina)