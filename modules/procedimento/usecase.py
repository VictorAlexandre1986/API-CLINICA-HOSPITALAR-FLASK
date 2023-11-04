from datetime import datetime, time

class ProcedimentoUseCase:
    
    def __init__(self, procedimento_repository):
        self.procedimento_repository = procedimento_repository
        
    
    def criar_procedimento(self, id: int, data: datetime, hora: time, procedimento: str, medico: str, auxiliar: str):
        return self.procedimento_repository.criar_procedimento(id, data, hora, procedimento, medico, auxiliar)
    
    def buscar_procedimento_por_id(self, id: int):
        return self.procedimento_repository.buscar_procedimento_por_id(id)
    
    def buscar_procedimentos(self):
        return self.procedimento_repository.buscar_procedimentos()
    
    def deletar_procedimento(self, id: int):
        return self.procedimento_repository.deletar_procedimento(id)
    
    def atualizar_procedimento(self, id: int, data: datetime, hora: time, procedimento: str, medico: str, auxiliar: str):
        return self.procedimento_repository.atualizar_procedimento(id, data, hora, procedimento, medico, auxiliar)