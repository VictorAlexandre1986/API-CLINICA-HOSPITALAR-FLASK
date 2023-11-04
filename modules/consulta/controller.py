from modules.consulta.dto import ConsultaDTO
from modules.consulta.repository.data_base.consulta_repo import ConsultaRepository
from modules.consulta.usecase import ConsultaUseCase


class consultaController:

    @staticmethod
    def criar_consulta(data: dict):
        data_dto = ConsultaDTO(**data)
        repository = ConsultaRepository()
        result = ConsultaUseCase(repository).criar_consulta(id = data_dto.id, data = data_dto.data, hora = data_dto.hora, procedimento = data_dto.procedimento, exame = data_dto.exame, vacina = data_dto.vacina, medico = data_dto.medico, auxiliar= data_dto.auxiliar)
        return result
    
    @staticmethod
    def buscar_consulta_por_id(id: int):
        repository = ConsultaRepository()
        result = ConsultaUseCase(repository).buscar_consulta_por_id(id)
        return result
    
    @staticmethod
    def buscar_consultas():
        repository = ConsultaRepository()
        result = ConsultaUseCase(repository).buscar_consultas()
        result = [consulta.dict() for consulta in result]
        return result
    
    @staticmethod
    def atualizar_consulta(data: dict, id: int):
        data_dto = ConsultaDTO(**data)
        repository = ConsultaRepository()
        result = ConsultaUseCase(repository).atualizar_consulta(id = data_dto.id, data = data_dto.data, hora = data_dto.hora, procedimento = data_dto.procedimento, exame = data_dto.exame, vacina = data_dto.vacina, medico = data_dto.medico, auxiliar= data_dto.auxiliar)
        return result
    
    @staticmethod
    def deletar_consulta(id: int):
        repository = ConsultaRepository()
        result = ConsultaUseCase(repository).deletar_consulta(id)
        return result