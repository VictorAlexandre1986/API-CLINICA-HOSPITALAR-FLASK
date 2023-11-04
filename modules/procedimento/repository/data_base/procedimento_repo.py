from infra.db.db_config import DBConnectionHandler
from modules.procedimento.repository.data_base.interface import ProcedimentoRepositoryInterface
from modules.procedimento.repository.data_base.model import Procedimento
from modules.procedimento.dto import ProcedimentoDTO
from datetime import datetime, time
import uuid as uuid


class ProcedimentoRepository(ProcedimentoRepositoryInterface):

    def _criar_procedimento_objeto(self, procedimento):
        return ProcedimentoDTO(
            id = procedimento.id,
            procedimento = procedimento.procedimento,
            preco = procedimento.preco
        )

    def criar_procedimento(self, id: int, procedimento: str, preco: float):
        try:
            with DBConnectionHandler() as db_connection:
                novo_procedimento = Procedimento(id=id, procedimento = procedimento, preco = preco)
                db_connection.session.add(novo_procedimento)
                db_connection.session.commit()
                return self._criar_procedimento_objeto(novo_procedimento)
        except Exception as exc:
            raise exc

    def buscar_procedimento_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Procedimento).filter(Procedimento.id == id).one_or_none()
            data_resultado = self._criar_procedimento_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_procedimentos(self):
        with DBConnectionHandler() as db_connection:
            list_procedimentos = []
            procedimentos = db_connection.session.query(Procedimento).all()
            for procedimento in procedimentos:
                list_procedimentos.append(
                    self._criar_procedimento_objeto(procedimento)
                )
            return list_procedimentos
        
    def atualizar_procedimento(self, id: int, procedimento: str, preco: float):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Procedimento).filter(Procedimento.id == id).one_or_none()
            if data:
                data.id = id
                data.procedimento = procedimento
                data.preco = preco
                db_connection.session.commit()
                return self._criar_procedimento_objeto(data)
            return None

    def deletar_procedimento(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Procedimento).filter(Procedimento.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_procedimento_objeto(data)
            return data