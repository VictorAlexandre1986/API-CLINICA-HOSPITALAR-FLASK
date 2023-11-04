from datetime import datetime, time

class ConsultaUseCase:
    
    def __init__(self, consulta_repository):
        self.consulta_repository = consulta_repository
        
    
    def criar_consulta(self, id: int, data: datetime, hora: time, procedimento: int, medico: str, auxiliar: str):
        return self.consulta_repository.criar_consulta(id, data, hora, procedimento, medico, auxiliar)
    
    def buscar_consulta_por_id(self, id: int):
        return self.consulta_repository.buscar_consulta_por_id(id)
    
    def buscar_consultas(self):
        return self.consulta_repository.buscar_consultas()
    
    def deletar_consulta(self, id: int):
        return self.consulta_repository.deletar_consulta(id)
    
    def atualizar_consulta(self, id: int, data: datetime, hora: time, consulta: str, medico: str, auxiliar: str):
        return self.consulta_repository.atualizar_consulta(id, data, hora, consulta, medico, auxiliar)