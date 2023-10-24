from modules.agenda.dto import AgendaDTO
from modules.agenda.repository.data_base.agenda_repo import AgendaRepository
from modules.agenda.usecase import AgendaUseCase



class AgendaController:

    @staticmethod
    def criar_agenda(data: dict):
        data_dto = AgendaDTO(**data)
        repository = AgendaRepository()
        result = AgendaUseCase(repository).criar_agenda(id = data_dto.id, cpf = data_dto.cpf, dia = data_dto.dia, hora = data_dto.hora, procedimento = data_dto.procedimento, medico= data_dto.medico)
        return result
    
    @staticmethod
    def buscar_agenda_por_id(id: int):
        repository = AgendaRepository()
        result = AgendaUseCase(repository).buscar_agenda_por_id(id)
        return result
    
    @staticmethod
    def buscar_agendas():
        repository = AgendaRepository()
        result = AgendaUseCase(repository).buscar_agendas()
        result = [agenda.dict() for agenda in result]
        return result
    
    @staticmethod
    def atualizar_agenda(data: dict, id: int):
        data_dto = AgendaDTO(**data)
        repository = AgendaRepository()
        result = AgendaUseCase(repository).atualizar_agenda(id = id, cpf = data_dto.cpf, dia = data_dto.dia, hora = data_dto.hora, procedimento = data_dto.procedimento, medico= data_dto.medico)
        return result
    
    @staticmethod
    def deletar_agenda(id: int):
        repository = AgendaRepository()
        result = AgendaUseCase(repository).deletar_agenda(id)
        return result