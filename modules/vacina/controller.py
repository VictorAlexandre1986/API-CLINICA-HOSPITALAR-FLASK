from modules.vacina.dto import VacinaDTO
from modules.vacina.repository.data_base.vacina_repo import VacinaRepository
from modules.vacina.usecase import VacinaUseCase


class VacinaController:

    @staticmethod
    def criar_vacina(data: dict):
        data_dto = VacinaDTO(**data)
        repository = VacinaRepository()
        result = VacinaUseCase(repository).criar_vacina(id = data_dto.id, nome = data_dto.nome, proposito = data_dto.proposito, ml = data_dto.ml, estoque = data_dto.estoque, vencimento= data_dto.vencimento)
        return result
    
    @staticmethod
    def buscar_vacina_por_id(id: int):
        repository = VacinaRepository()
        result = VacinaUseCase(repository).buscar_vacina_por_id(id)
        return result
    
    @staticmethod
    def buscar_vacinas():
        repository = VacinaRepository()
        result = VacinaUseCase(repository).buscar_vacinas()
        vacinas = [vacina.dict() for vacina in result]
        lista_vacina=[]
        for vacina in vacinas:
            vacina['vencimento'] = vacina['vencimento'].strftime("%d/%m/%Y %H:%M:%S") 
            lista_vacina.append(vacina)
        return lista_vacina
    
    @staticmethod
    def atualizar_vacina(data: dict, id: int):
        data_dto = VacinaDTO(**data)
        repository = VacinaRepository()
        result = VacinaUseCase(repository).atualizar_vacina(id = id, nome = data_dto.nome, proposito = data_dto.proposito, ml = data_dto.ml, estoque = data_dto.estoque, vencimento= data_dto.vencimento)
        return result
    
    @staticmethod
    def deletar_vacina(id: int):
        repository = VacinaRepository()
        result = VacinaUseCase(repository).deletar_vacina(id)
        return result