from datetime import datetime,time

class PacienteUseCase:
    
    def __init__(self, paciente_repository):
        self.paciente_repository = paciente_repository
        
    
    def criar_paciente(self, id: int, nome:str, cpf: str, sexo: str, endereco: str, num: str, bairro: str, cidade: str, contato: str, contato2: str, email:str):
        return self.paciente_repository.criar_paciente(id, nome, cpf, sexo, endereco, num, bairro, cidade, contato, contato2, email)
    
    def buscar_paciente_por_id(self, id: int):
        return self.paciente_repository.buscar_paciente_por_id(id)
    
    def buscar_pacientes(self):
        return self.paciente_repository.buscar_pacientes()
    
    def deletar_paciente(self, id: int):
        return self.paciente_repository.deletar_paciente(id)
    
    def atualizar_paciente(self, id: int, nome:str, cpf: str, sexo: str, endereco: str, num: str, bairro: str, cidade: str, contato: str, contato2: str, email:str):
        return self.paciente_repository.atualizar_paciente(id, nome, cpf, sexo, endereco, num, bairro, cidade, contato, contato2, email)