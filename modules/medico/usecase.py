from datetime import datetime,time

class MedicoUseCase:
    
    def __init__(self, medico_repository):
        self.medico_repository = medico_repository
        
    
    def criar_medico(self, id: int, nome: str, crm:str , especialidade:str, contato:str, id_login: int):
        return self.medico_repository.criar_medico(id, nome, crm, especialidade, contato, id_login)
    
    def buscar_medico_por_id(self, id: int):
        return self.medico_repository.buscar_medico_por_id(id)
    
    def buscar_medicos(self):
        return self.medico_repository.buscar_medicos()
    
    def deletar_medico(self, id: int):
        return self.medico_repository.deletar_medico(id)
    
    def atualizar_medico(self, id: int, nome: str, crm:str , especialidade:str, contato:str, id_login: int):
        return self.medico_repository.atualizar_medico(id, nome, crm, especialidade, contato, id_login)