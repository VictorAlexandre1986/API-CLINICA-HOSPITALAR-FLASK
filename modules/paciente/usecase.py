from datetime import datetime,time

class PacienteUseCase:
    
    def __init__(self, paciente_repository):
        self.paciente_repository = paciente_repository
        
    
    def criar_paciente(self, id: int, nome:str, cpf: str, sexo: str, dt_nasc: datetime, endereco: str, bairro: str, cidade: str, contato: str, estado: str, id_login: int):
        return self.paciente_repository.criar_paciente(id, nome, cpf, sexo, dt_nasc, endereco, bairro, cidade, estado, contato, id_login)
    
    def buscar_paciente_por_id(self, id: int):
        return self.paciente_repository.buscar_paciente_por_id(id)
    
    def buscar_pacientes(self):
        return self.paciente_repository.buscar_pacientes()
    
    def deletar_paciente(self, id: int):
        return self.paciente_repository.deletar_paciente(id)
    
    def atualizar_paciente(self, id: int, nome:str, cpf: str, dt_nasc:datetime, sexo: str, endereco: str, bairro: str, cidade: str, estado: str, contato: str, id_login: int):
        return self.paciente_repository.atualizar_paciente(id, nome, cpf, sexo, dt_nasc, endereco, bairro, cidade, estado, contato, id_login)