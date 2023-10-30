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
            data = procedimento.data,
            hora = procedimento.hora,
            procedimento = procedimento.procedimento,
            medico = procedimento.medico,
            auxiliar = procedimento.auxiliar
        )

    def criar_procedimento(self, id: int, data: datetime, hora: time, procedimento: str, medico: str, auxiliar: str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_procedimento = Procedimento(id=id, data = data, hora = hora, procedimento = procedimento, medico = medico, auxiliar = auxiliar)
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
        
    def atualizar_procedimento(self, id: int, data: datetime, hora: time, procedimento: str, medico: str, auxiliar: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Procedimento).filter(Procedimento.id == id).one_or_none()
            if data:
                data.id = id
                data.data = data
                data.hora = hora
                data.procedimento = procedimento
                data.medico = medico
                data.auxiliar = auxiliar
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