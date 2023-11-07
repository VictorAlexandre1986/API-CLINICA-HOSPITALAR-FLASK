from modules.pagamento.dto import PagamentoDTO
from modules.pagamento.repository.data_base.pagamento_repo import PagamentoRepository
from modules.pagamento.usecase import PagamentoUseCase


class PagamentoController:

    @staticmethod
    def criar_pagamento(data: dict):
        data_dto = PagamentoDTO(**data)
        repository = PagamentoRepository()
        result = PagamentoUseCase(repository).criar_pagamento(id = data_dto.id, id_paciente= data_dto.id_paciente, data= data_dto.data, descricao_procedimentos=data_dto.procedimento, descricao_exames=data_dto.exame, descricao_vacinas= data_dto.vacina, preco=data_dto.preco)
        return result
    
    @staticmethod
    def buscar_pagamento_por_id(id: int):
        repository = PagamentoRepository()
        result = PagamentoUseCase(repository).buscar_pagamento_por_id(id)
        return result
    

    @staticmethod
    def buscar_pagamentos():
        repository = PagamentoRepository()
        result = PagamentoUseCase(repository).buscar_pagamentos()
        result = [pagamento.dict() for pagamento in result]
        return result
    
    @staticmethod
    def atualizar_pagamento(data: dict, id: int):
        data_dto = PagamentoDTO(**data)
        repository = PagamentoRepository()
        result = PagamentoUseCase(repository).atualizar_pagamento(id = id, id_paciente= data_dto.id_paciente, data= data_dto.data, descricao_procedimento=data_dto.procedimento, descricao_exame=data_dto.exame, descricao_vacina= data_dto.vacina, preco=data_dto.preco)
        return result
    
    @staticmethod
    def deletar_pagamento(id: int):
        repository = PagamentoRepository()
        result = PagamentoUseCase(repository).deletar_pagamento(id)
        return result