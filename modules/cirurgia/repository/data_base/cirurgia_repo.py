from infra.db.db_config import DBConnectionHandler
from modules.cirurgia.repository.data_base.interface import CirurgiaRepositoryInterface
from modules.cirurgia.repository.data_base.model import Cirurgia
from modules.cirurgia.dto import CirurgiaDTO
from datetime import datetime, time
import uuid as uuid


class CirurgiaRepository(CirurgiaRepositoryInterface):

    def _criar_cirurgia_objeto(self, cirurgia):
        return CirurgiaDTO(
            id = cirurgia.id,
            nome_cirurgia = cirurgia.nome_cirurgia,
        )

    def criar_cirurgia(self, id: int, nome_cirurgia: str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_cirurgia = Cirurgia(id= id, nome_cirurgia= nome_cirurgia)
                db_connection.session.add(novo_cirurgia)
                db_connection.session.commit()
                return self._criar_cirurgia_objeto(novo_cirurgia)
        except Exception as exc:
            raise exc

    def buscar_cirurgia_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cirurgia).filter(Cirurgia.id == id).one_or_none()
            data_resultado = self._criar_cirurgia_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_cirurgias(self):
        with DBConnectionHandler() as db_connection:
            list_cirurgias = []
            cirurgias = db_connection.session.query(Cirurgia).all()
            for cirurgia in cirurgias:
                list_cirurgias.append(
                    self._criar_cirurgia_objeto(cirurgia)
                )
            return list_cirurgias
        
    def atualizar_cirurgia(self, id: int, nome_cirurgia: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cirurgia).filter(Cirurgia.id == id).one_or_none()
            if data:
                data.id = id
                data.nome_cirurgia = nome_cirurgia
                db_connection.session.commit()
                return self._criar_cirurgia_objeto(data)
            return None

    def deletar_cirurgia(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Cirurgia).filter(Cirurgia.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_cirurgia_objeto(data)
            return data
        