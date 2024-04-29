from datetime import datetime, time

class ProcedimentoUseCase:
    
    def __init__(self, procedimento_repository):
        self.procedimento_repository = procedimento_repository
        
    
    def criar_procedimento(self, id: int, procedimento: str, id_exame: int, id_vacina: int, id_cirurgia: int, id_medico: int, id_paciente: int, id_auxiliar: int):
        return self.procedimento_repository.criar_procedimento(id, procedimento, id_exame, id_vacina, id_cirurgia, id_medico, id_paciente, id_auxiliar)
    
    def buscar_procedimento_por_id(self, id: int):
        return self.procedimento_repository.buscar_procedimento_por_id(id)

    def buscar_procedimento_por_id_paciente(self, id_paciente: int):
        return self.procedimento_repository.buscar_procedimento_por_id_paciente(id_paciente)
    
    def buscar_procedimentos(self):
        return self.procedimento_repository.buscar_procedimentos()
    
    def deletar_procedimento(self, id: int):
        return self.procedimento_repository.deletar_procedimento(id)
    
    def atualizar_procedimento(self, id: int,  procedimento: str, id_exame: int, id_vacina: int, id_cirurgia: int, id_medico: int, id_paciente: int, id_auxiliar: int):
        return self.procedimento_repository.atualizar_procedimento(id, procedimento, id_exame, id_vacina, id_cirurgia, id_medico, id_paciente, id_auxiliar)