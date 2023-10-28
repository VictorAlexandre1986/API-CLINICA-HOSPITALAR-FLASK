from datetime import datetime,time

class ProntuarioUseCase:
    
    def __init__(self, prontuario_repository):
        self.prontuario_repository = prontuario_repository
        
    
    def criar_prontuario(self, id: int, cpf: str, procedimento: int, vacina: int):
        return self.prontuario_repository.criar_prontuario(id, cpf, procedimento, vacina)
    
    def buscar_prontuario_por_id(self, id: int):
        return self.prontuario_repository.buscar_prontuario_por_id(id)
    
    def buscar_prontuarios(self):
        return self.prontuario_repository.buscar_prontuarios()
    
    def deletar_prontuario(self, id: int):
        return self.prontuario_repository.deletar_prontuario(id)
    
    def atualizar_prontuario(self,id:int, cpf: str, procedimento:str, vacina: int):
        return self.prontuario_repository.atualizar_prontuario(id, cpf, procedimento, vacina)