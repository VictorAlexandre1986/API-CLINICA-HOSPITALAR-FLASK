from infra.db.db_config import DBConnectionHandler
from modules.pagamento.repository.data_base.interface import PagamentoRepositoryInterface
from modules.pagamento.repository.data_base.model import Pagamento
from modules.procedimento.repository.data_base.model import Procedimento
from modules.exame.repository.data_base.model import Exame
from modules.exame.repository.data_base.model import Vacina
from modules.pagamento.dto import PagamentoDTO,Pagamento_procedimentoDTO,Pagamento_exameDTO,Pagamento_vacinaDTO
from datetime import datetime, time
import uuid as uuid
from typing import List

class PagamentoRepository(PagamentoRepositoryInterface):

    def _criar_pagamento_objeto(self, pagamento):
        return PagamentoDTO(
            id = pagamento.id,
            pagamento = pagamento.pagamento,
            preco = pagamento.preco
        )
        
    def _criar_preco_procedimento(self, procedimento):
        return Pagamento_procedimentoDTO(
            preco = procedimento.preco
        )
        
    def _criar_preco_exame(self, exame):
        return Pagamento_exameDTO(
            preco = exame.preco
        )
        
    def _criar_preco_vacina(self, vacina):
        return Pagamento_vacinaDTO(
            preco = vacina.preco
        )
        
    def _criar_descricao_vacina(self, vacina):
        return Pagamento_vacinaDTO(
            descricao=f'{vacina.nome} = R${vacina.preco}\n'
        )
        
    def _criar_descricao_exame(self, exame):
        return Pagamento_exameDTO(
            descricao=f'{exame.nome} = R${exame.preco}\n'
        )
        
    def _criar_descricao_procedimento(self, procedimento):
        return Pagamento_procedimentoDTO(
            descricao=f'{procedimento.nome} = R${procedimento.preco}\n'
        )


    def criar_pagamento(self, id: int, id_paciente: int, data: datetime, procedimentos: List[str], exames: List[str], vacinas: List[str],pagamento: str, preco: float):
        try:
            valor_procedimentos = 0
            valor_exames = 0
            valor_vacinas = 0
            descricao_procedimentos = ''
            descricao_exames =''
            descricao_vacinas=''
            
            with DBConnectionHandler() as db_connection:
                #Somatória dos valores dos procedimentos
                if len(procedimentos)>0:
                    for procedimento in procedimentos:
                        procedimento = db_connection.session.query(Procedimento).filter(Procedimento.str == procedimento).one_or_none()
                        valor_procedimentos += int(self._criar_preco_procedimento(procedimento.preco))
                        descricao_procedimentos += (self._criar_descricao_procedimento(procedimento.descricao, procedimento.preco))
                
                #Somatória dos valores dos exames
                if len(exames)>0:
                    for exame in exames:
                        exame = db_connection.session.query(Exame).filter(Exame.str == exame).one_or_none()
                        valor_exames += int(self._criar_preco_exame(exame.preco))
                        descricao_exames  += (self._criar_descricao_exame(exame.descricao, exame.preco))

                #Somatória dos valores das vacinas
                if len(vacinas)>0:
                    for vacina in vacinas:
                        vacina = db_connection.session.query(Vacina).filter(Vacina.str == vacina).one_or_none()
                        valor_vacinas += int(self._criar_preco_vacina(vacina.preco))
                        descricao_vacinas += (self._criar_descricao_vacina(vacina.descricao, vacina.preco))
                
                
                preco = valor_procedimentos + valor_exames + valor_vacinas
                
                novo_pagamento = Pagamento(id=id, id_paciente = id_paciente, data = data, descricao_procedimentos = descricao_procedimentos, descricao_exames = descricao_exames, descricao_vacinas = descricao_vacinas , preco = preco)
                db_connection.session.add(novo_pagamento)
                db_connection.session.commit()
                return self._criar_pagamento_objeto(novo_pagamento)
        except Exception as exc:
            raise exc

    def buscar_pagamento_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Pagamento).filter(Pagamento.id == id).one_or_none()
            data_resultado = self._criar_pagamento_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_pagamentos(self):
        with DBConnectionHandler() as db_connection:
            list_pagamentos = []
            pagamentos = db_connection.session.query(Pagamento).all()
            for pagamento in pagamentos:
                list_pagamentos.append(
                    self._criar_pagamento_objeto(pagamento)
                )
            return list_pagamentos
        
    def atualizar_pagamento(self, id: int, id_paciente: int , data: datetime, descricao_procedimentos: str , descricao_exames:str , descricao_vacinas: str , preco: float):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Pagamento).filter(Pagamento.id == id).one_or_none()
            if data:
                data.id = id
                data.id_paciente = id_paciente
                data.data = data
                data.descricao_procedimentos = descricao_procedimentos
                data.descricao_exames = descricao_exames
                data.descricao_vacinas = descricao_vacinas
                data.preco = preco
                db_connection.session.commit()
                return self._criar_pagamento_objeto(data)
            return None

    def deletar_pagamento(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Pagamento).filter(Pagamento.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_pagamento_objeto(data)
            return data