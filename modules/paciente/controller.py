from modules.paciente.dto import PacienteDTO
from modules.paciente.repository.data_base.paciente_repo import PacienteRepository
from modules.paciente.usecase import PacienteUseCase
from datetime import datetime


class PacienteController:

    @staticmethod
    def criar_paciente(data: dict):
        data_dto = PacienteDTO(**data)
        repository = PacienteRepository()
        result = PacienteUseCase(repository).criar_paciente(id = data_dto.id, nome= data_dto.nome, cpf = data_dto.cpf, sexo= data_dto.sexo, dt_nasc = data_dto.dt_nasc, endereco= data_dto.endereco,  bairro = data_dto.bairro, cidade= data_dto.cidade, estado= data_dto.estado, contato= data_dto.contato, id_login = data_dto.id_login)
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
        lista_pacientes=[]
        for paciente in result:
            paciente['dt_nasc'] = paciente['dt_nasc'].strftime("%d/%m/%Y %H:%M:%S")
            lista_pacientes.append(paciente)
        return lista_pacientes
    
    @staticmethod
    def atualizar_paciente(data: dict, id: int):
        data_dto = PacienteDTO(**data)
        repository = PacienteRepository()
        result = PacienteUseCase(repository).atualizar_paciente(id = data_dto.id, nome= data_dto.nome, cpf = data_dto.cpf, sexo= data_dto.sexo, dt_nasc=data_dto.dt_nasc, endereco= data_dto.endereco, bairro = data_dto.bairro, cidade= data_dto.cidade,  estado= data_dto.estado, contato= data_dto.contato, id_login = data_dto.id_login)
        return result
    
    @staticmethod
    def deletar_paciente(id: int):
        repository = PacienteRepository()
        result = PacienteUseCase(repository).deletar_paciente(id)
        return result