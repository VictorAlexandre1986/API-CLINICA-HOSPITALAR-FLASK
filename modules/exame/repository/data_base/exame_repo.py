from infra.db.db_config import DBConnectionHandler
from modules.exame.repository.data_base.interface import ExameRepositoryInterface
from modules.exame.repository.data_base.model import Exame
from modules.exame.dto import ExameDTO
from datetime import datetime, time
import uuid as uuid


class ExameRepository(ExameRepositoryInterface):

    def _criar_exame_objeto(self, dto_exame):
        return ExameDTO(
            id = dto_exame.id,
            tipo_exame = dto_exame.tipo_exame,
            valor = dto_exame.valor
        )

    def criar_exame(self, id: int, tipo_exame: str, valor: float):
        try:
            with DBConnectionHandler() as db_connection:
                novo_exame = Exame(id=id, tipo_exame=tipo_exame, valor=valor)
                db_connection.session.add(novo_exame)
                db_connection.session.commit()
                return self._criar_exame_objeto(novo_exame)
        except Exception as exc:
            raise exc

    def buscar_exame_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Exame).filter(Exame.id == id).one_or_none()
            data_resultado = self._criar_exame_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_exames(self):
        with DBConnectionHandler() as db_connection:
            list_exames = []
            exames = db_connection.session.query(Exame).all()
            for exame in exames:
                list_exames.append(
                    self._criar_exame_objeto(exame)
                )
            return list_exames
        
    def atualizar_exame(self, id: int, tipo_exame: str, valor: float):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Exame).filter(Exame.id == id).one_or_none()
            if data:
                data.id = id
                data.tipo_exame = tipo_exame
                data.valor = valor
                db_connection.session.commit()
                return self._criar_exame_objeto(data)
            return None

    def deletar_exame(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Exame).filter(Exame.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_exame_objeto(data)
            return data