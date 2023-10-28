from modules.prontuario.dto import ProntuarioDTO
from modules.prontuario.repository.data_base.prontuario_repo import ProntuarioRepository
from modules.prontuario.usecase import ProntuarioUseCase
from datetime import datetime


class ProntuarioController:

    @staticmethod
    def criar_prontuario(data: dict):
        data_dto = ProntuarioDTO(**data)
        repository = ProntuarioRepository()
        result = ProntuarioUseCase(repository).criar_prontuario(id = data_dto.id, cpf = data_dto.cpf, procedimento = data_dto.procedimento, vacina= data_dto.vacina)
        return result
    
    @staticmethod
    def buscar_prontuario_por_id(id: int):
        repository = ProntuarioRepository()
        result = ProntuarioUseCase(repository).buscar_prontuario_por_id(id)
        return result
    
    @staticmethod
    def buscar_prontuarios():
        repository = ProntuarioRepository()
        result = ProntuarioUseCase(repository).buscar_prontuarios()
        result = [prontuario.dict() for prontuario in result]
        return result
    
    @staticmethod
    def atualizar_prontuario(data: dict, id: int):
        data_dto = ProntuarioDTO(**data)
        repository = ProntuarioRepository()
        result = ProntuarioUseCase(repository).atualizar_prontuario(id = id, cpf = data_dto.cpf, procedimento = data_dto.procedimento, vacina= data_dto.vacina)
        return result
    
    @staticmethod
    def deletar_prontuario(id: int):
        repository = ProntuarioRepository()
        result = ProntuarioUseCase(repository).deletar_prontuario(id)
        return result