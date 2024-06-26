from modules.login.dto import LoginDTO
from modules.login.repository.login_repo import LoginRepository
from modules.login.usecase import LoginUseCase



class LoginController:

    @staticmethod
    def criar_login(data: dict):
        data_dto = LoginDTO(**data)
        repository = LoginRepository()
        result = LoginUseCase(repository).criar_login(id = data_dto.id, usuario = data_dto.usuario, senha = data_dto.senha)
        return result
    
    @staticmethod
    def buscar_login_por_id(id: int):
        repository = LoginRepository()
        result = LoginUseCase(repository).buscar_login_por_id(id)
        return result
    
    @staticmethod
    def buscar_logins():
        repository = LoginRepository()
        result = LoginUseCase(repository).buscar_logins()
        result = [login.dict() for login in result]
        return result
    
    @staticmethod
    def atualizar_login(data: dict, id: int):
        data_dto = LoginDTO(**data)
        repository = LoginRepository()
        result = LoginUseCase(repository).atualizar_login(id = id, usuario = data_dto.usuario, senha = data_dto.senha)
        return result
    
    @staticmethod
    def deletar_login(id: int):
        repository = LoginRepository()
        result = LoginUseCase(repository).deletar_login(id)
        return result