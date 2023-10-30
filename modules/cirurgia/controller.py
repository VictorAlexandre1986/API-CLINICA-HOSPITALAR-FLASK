from modules.cirurgia.dto import CirurgiaDTO
from modules.cirurgia.repository.data_base.cirurgia_repo import CirurgiaRepository
from modules.cirurgia.usecase import CirurgiaUseCase
from datetime import datetime


class CirurgiaController:

    @staticmethod
    def criar_cirurgia(data: dict):
        data_dto = CirurgiaDTO(**data)
        repository = CirurgiaRepository()
        result = CirurgiaUseCase(repository).criar_cirurgia(id = data_dto.id, nome_cirurgia = data_dto.nome_cirurgia)
        return result
    
    @staticmethod
    def buscar_cirurgia_por_id(id: int):
        repository = CirurgiaRepository()
        result = CirurgiaUseCase(repository).buscar_cirurgia_por_id(id)
        return result
    
    @staticmethod
    def buscar_cirurgias():
        repository = CirurgiaRepository()
        result = CirurgiaUseCase(repository).buscar_cirurgias()
        result = [cirurgia.dict() for cirurgia in result]
        return result
    
    @staticmethod
    def atualizar_cirurgia(data: dict, id: int):
        data_dto = CirurgiaDTO(**data)
        repository = CirurgiaRepository()
        result = CirurgiaUseCase(repository).atualizar_cirurgia(id = id, cirurgia = data_dto.nome_cirurgia)
        return result
    
    @staticmethod
    def deletar_cirurgia(id: int):
        repository = CirurgiaRepository()
        result = CirurgiaUseCase(repository).deletar_cirurgia(id)
        return result