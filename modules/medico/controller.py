from modules.medico.dto import MedicoDTO
from modules.medico.repository.data_base.medico_repo import MedicoRepository
from modules.medico.usecase import MedicoUseCase



class MedicoController:

    @staticmethod
    def criar_medico(data: dict):
        data_dto = MedicoDTO(**data)
        repository = MedicoRepository()
        result = MedicoUseCase(repository).criar_medico(id = data_dto.id, nome = data_dto.nome, crm = data_dto.crm, especialidade = data_dto.especialidade, contato = data_dto.contato, id_login = data_dto.id_login)
        return result
    
    @staticmethod
    def buscar_medico_por_id(id: int):
        repository = MedicoRepository()
        result = MedicoUseCase(repository).buscar_medico_por_id(id)
        return result
    
    @staticmethod
    def buscar_medicos():
        repository = MedicoRepository()
        result = MedicoUseCase(repository).buscar_medicos()
        result = [login.dict() for login in result]
        return result
    
    @staticmethod
    def atualizar_medico(data: dict, id: int):
        data_dto = MedicoDTO(**data)
        repository = MedicoRepository()
        result = MedicoUseCase(repository).atualizar_medico(id = data_dto.id, nome = data_dto.nome, crm = data_dto.crm, especialidade = data_dto.especialidade, contato = data_dto.contato, id_login=data_dto.id_login)
        return result
    
    @staticmethod
    def deletar_medico(id: int):
        repository = MedicoRepository()
        result = MedicoUseCase(repository).deletar_medico(id)
        return result