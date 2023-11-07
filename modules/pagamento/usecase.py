from datetime import datetime, time
from typing import List

class PagamentoUseCase:
    
    def __init__(self, pagamento_repository):
        self.pagamento_repository = pagamento_repository
        
    
    def criar_pagamento(self, id: int, id_paciente:int, data: datetime, descricao_procedimentos: List[str], descricao_exames: List[str], descricao_vacinas: List[str], preco: float):        
        return self.pagamento_repository.criar_pagamento(id, id_paciente, data, descricao_procedimentos, descricao_exames, descricao_vacinas, preco)
    
    def buscar_pagamento_por_id(self, id: int):
        return self.pagamento_repository.buscar_pagamento_por_id(id)
    
    def buscar_pagamentos(self):
        return self.pagamento_repository.buscar_pagamentos()
    
    def deletar_pagamento(self, id: int):
        return self.pagamento_repository.deletar_pagamento(id)
    
    def atualizar_pagamento(self, id: int, id_paciente:int, data: datetime, descricao_procedimentos: List[str], descricao_exames: List[str], descricao_vacinas: [str], preco: float):
        return self.pagamento_repository.atualizar_pagamento(id, id_paciente, data, descricao_procedimentos, descricao_exames, descricao_vacinas, preco)