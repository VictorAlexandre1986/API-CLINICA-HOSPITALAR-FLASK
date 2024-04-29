from datetime import datetime,time

class AgendaUseCase:
    
    def __init__(self, agenda_repository):
        self.agenda_repository = agenda_repository
        
    
    def criar_agenda(self, id: int, cpf: str, dia:datetime, id_procedimento: int, id_medico: int, id_cirurgia: int):
        return self.agenda_repository.criar_agenda(id, cpf, dia, id_procedimento, id_medico, id_cirurgia)
    
    def buscar_agenda_por_id(self, id: int):
        return self.agenda_repository.buscar_agenda_por_id(id)
    
    def buscar_agendas(self):
        return self.agenda_repository.buscar_agendas()
    
    def deletar_agenda(self, id: int):
        return self.agenda_repository.deletar_agenda(id)
    
    def atualizar_agenda(self,id:int, cpf: str, dia: datetime, id_procedimento: int, id_medico: int, id_cirurgia: int):
        return self.agenda_repository.atualizar_agenda(id,  cpf, dia, id_procedimento, id_medico, id_cirurgia)