from modules.exame.dto import ExameDTO
from modules.exame.repository.data_base.exame_repo import ExameRepository
from modules.exame.usecase import ExameUseCase


class ExameController:

    @staticmethod
    def criar_exame(data: dict):
        data_dto = ExameDTO(**data)
        repository = ExameRepository()
        result = ExameUseCase(repository).criar_exame(id = data_dto.id, tipo_exame = data_dto.tipo_exame, valor = data_dto.valor)
        print(result)
        return result
    
    @staticmethod
    def buscar_exame_por_id(id: int):
        repository = ExameRepository()
        result = ExameUseCase(repository).buscar_exame_por_id(id)
        return result
    
    @staticmethod
    def buscar_exames():
        repository = ExameRepository()
        result = ExameUseCase(repository).buscar_exames()
        result = [exame.dict() for exame in result]
        return result
    
    @staticmethod
    def atualizar_exame(data: dict, id: int):
        data_dto = ExameDTO(**data)
        repository = ExameRepository()
        result = ExameUseCase(repository).atualizar_exame(id = data_dto.id, tipo_exame = data_dto.tipo_exame, valor = data_dto.valor)
        return result
    
    @staticmethod
    def deletar_exame(id: int):
        repository = ExameRepository()
        result = ExameUseCase(repository).deletar_exame(id)
        return result