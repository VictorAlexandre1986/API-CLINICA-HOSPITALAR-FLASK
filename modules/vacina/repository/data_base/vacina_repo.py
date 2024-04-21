from infra.db.db_config import DBConnectionHandler
from modules.vacina.repository.data_base.interface import VacinaRepositoryInterface
from modules.vacina.repository.data_base.model import Vacina
from modules.vacina.dto import VacinaDTO
from datetime import datetime, time
import uuid as uuid


class VacinaRepository(VacinaRepositoryInterface):

    def _criar_vacina_objeto(self, vacina):
        return VacinaDTO(
            id = vacina.id,
            nome = vacina.nome,
            proposito = vacina.proposito,
            ml = vacina.ml,
            estoque = vacina.estoque,
            vencimento = vacina.vencimento
        )

    def criar_vacina(self, id: int, nome: str, proposito:str, ml: float, estoque:int, vencimento:datetime):
        try:
            with DBConnectionHandler() as db_connection:
                nova_vacina = Vacina(id=id, nome=nome, proposito=proposito, ml=ml, estoque=estoque, vencimento=vencimento)
                db_connection.session.add(nova_vacina)
                db_connection.session.commit()
                return self._criar_vacina_objeto(nova_vacina)
        except Exception as exc:
            raise exc

    def buscar_vacina_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Vacina).filter(Vacina.id == id).one_or_none()
            data_resultado = self._criar_vacina_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_vacinas(self):
        with DBConnectionHandler() as db_connection:
            list_vacinas = []
            vacinas = db_connection.session.query(Vacina).all()
            for vacina in vacinas:
                list_vacinas.append(
                    self._criar_vacina_objeto(vacina)
                )
            return list_vacinas
        
    def atualizar_vacina(self, id: int, nome: str, proposito:str, ml: float, estoque:int, vencimento:datetime):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Vacina).filter(Vacina.id == id).one_or_none()
            if data:
                data.id = id
                data.nome = nome
                data.proposito = proposito
                data.ml = ml
                data.estoque = estoque
                data.vencimento = vencimento
                db_connection.session.commit()
                return self._criar_vacina_objeto(data)
            return None

    def deletar_vacina(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Vacina).filter(Vacina.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_vacina_objeto(data)
            return data