from modules.auxiliar.dto import AuxiliarDTO
from modules.auxiliar.repository.data_base.auxiliar_repo import AuxiliarRepository
from modules.auxiliar.usecase import AuxiliarUseCase
from datetime import datetime


class AuxiliarController:

    @staticmethod
    def criar_auxiliar(data: dict):
        data_dto = AuxiliarDTO(**data)
        repository = AuxiliarRepository()
        result = AuxiliarUseCase(repository).criar_auxiliar(id = data_dto.id,nome = data_dto.nome ,cpf = data_dto.cpf, endereco = data_dto.endereco, num= data_dto.num, cidade= data_dto.cidade, contato= data_dto.contato, contato2 = data_dto.contato2, coren = data_dto.coren)
        return result
    
    @staticmethod
    def buscar_auxiliar_por_id(id: int):
        repository = AuxiliarRepository()
        result = AuxiliarUseCase(repository).buscar_auxiliar_por_id(id)
        return result
    
    @staticmethod
    def buscar_auxiliars():
        repository = AuxiliarRepository()
        result = AuxiliarUseCase(repository).buscar_auxiliars()
        result = [auxiliar.dict() for auxiliar in result]
        return result
    
    @staticmethod
    def atualizar_auxiliar(data: dict, id: int):
        data_dto = AuxiliarDTO(**data)
        repository = AuxiliarRepository()
        result = AuxiliarUseCase(repository).atualizar_auxiliar(id =id, nome = data_dto.nome ,cpf = data_dto.cpf, endereco = data_dto.endereco, num= data_dto.num, cidade= data_dto.cidade, contato= data_dto.contato, contato2 = data_dto.contato2, coren = data_dto.coren)
        return result
    
    @staticmethod
    def deletar_auxiliar(id: int):
        repository = AuxiliarRepository()
        result = AuxiliarUseCase(repository).deletar_auxiliar(id)
        return result