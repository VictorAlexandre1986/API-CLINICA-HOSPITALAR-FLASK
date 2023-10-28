from datetime import datetime,time

class AgendaUseCase:
    
    def __init__(self, agenda_repository):
        self.agenda_repository = agenda_repository
        
    
    def criar_agenda(self, id: int, cpf: str, dia:datetime, hora:time, procedimento:str, medico:str):
        return self.agenda_repository.criar_agenda(id, cpf, dia, hora, procedimento, medico)
    
    def buscar_agenda_por_id(self, id: int):
        return self.agenda_repository.buscar_agenda_por_id(id)
    
    def buscar_agendas(self):
        return self.agenda_repository.buscar_agendas()
    
    def deletar_agenda(self, id: int):
        return self.agenda_repository.deletar_agenda(id)
    
    def atualizar_agenda(self,id:int, cpf: str, dia:datetime, hora:time, procedimento:str, medico:str):
        return self.agenda_repository.atualizar_agenda(id,  cpf, dia, hora, procedimento, medico)