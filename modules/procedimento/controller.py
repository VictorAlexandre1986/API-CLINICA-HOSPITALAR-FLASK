from modules.procedimento.dto import ProcedimentoDTO
from modules.procedimento.repository.data_base.procedimento_repo import ProcedimentoRepository
from modules.procedimento.usecase import ProcedimentoUseCase


class ProcedimentoController:

    @staticmethod
    def criar_procedimento(data: dict):
        data_dto = ProcedimentoDTO(**data)
        repository = ProcedimentoRepository()
        result = ProcedimentoUseCase(repository).criar_procedimento(id = data_dto.id, procedimento = data_dto.procedimento, preco = data_dto.preco)
        return result
    
    @staticmethod
    def buscar_procedimento_por_id(id: int):
        repository = ProcedimentoRepository()
        result = ProcedimentoUseCase(repository).buscar_procedimento_por_id(id)
        return result
    
    @staticmethod
    def buscar_procedimentos():
        repository = ProcedimentoRepository()
        result = ProcedimentoUseCase(repository).buscar_procedimentos()
        result = [procedimento.dict() for procedimento in result]
        return result
    
    @staticmethod
    def atualizar_procedimento(data: dict, id: int):
        data_dto = ProcedimentoDTO(**data)
        repository = ProcedimentoRepository()
        result = ProcedimentoUseCase(repository).atualizar_procedimento(id = data_dto.id, procedimento = data_dto.procedimento, preco = data_dto.preco)
        return result
    
    @staticmethod
    def deletar_procedimento(id: int):
        repository = ProcedimentoRepository()
        result = ProcedimentoUseCase(repository).deletar_procedimento(id)
        return result