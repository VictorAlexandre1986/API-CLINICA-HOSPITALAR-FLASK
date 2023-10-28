from modules.paciente.dto import PacienteDTO
from modules.paciente.repository.data_base.paciente_repo import PacienteRepository
from modules.paciente.usecase import PacienteUseCase
from datetime import datetime


class PacienteController:

    @staticmethod
    def criar_paciente(data: dict):
        data_dto = PacienteDTO(**data)
        repository = PacienteRepository()
        result = PacienteUseCase(repository).criar_paciente(id = data_dto.id, nome= data_dto.nome, cpf = data_dto.cpf, sexo= data_dto.sexo, endereco= data_dto.endereco, num = data_dto.num, bairro = data_dto.bairro, cidade= data_dto.cidade, contato= data_dto.contato, contato2= data_dto.contato2, email= data_dto.email)
        return result
    
    @staticmethod
    def buscar_paciente_por_id(id: int):
        repository = PacienteRepository()
        result = PacienteUseCase(repository).buscar_paciente_por_id(id)
        return result
    
    @staticmethod
    def buscar_pacientes():
        repository = PacienteRepository()
        result = PacienteUseCase(repository).buscar_pacientes()
        result = [paciente.dict() for paciente in result]
        return result
    
    @staticmethod
    def atualizar_paciente(data: dict, id: int):
        data_dto = PacienteDTO(**data)
        repository = PacienteRepository()
        result = PacienteUseCase(repository).atualizar_paciente(id = data_dto.id, nome= data_dto.nome, cpf = data_dto.cpf, sexo= data_dto.sexo, endereco= data_dto.endereco, num = data_dto.num, bairro = data_dto.bairro, cidade= data_dto.cidade, contato= data_dto.contato, contato2= data_dto.contato2, email= data_dto.email)
        return result
    
    @staticmethod
    def deletar_paciente(id: int):
        repository = PacienteRepository()
        result = PacienteUseCase(repository).deletar_paciente(id)
        return result