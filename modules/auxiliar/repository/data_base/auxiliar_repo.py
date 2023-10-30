from infra.db.db_config import DBConnectionHandler
from modules.auxiliar.repository.data_base.interface import AuxiliarRepositoryInterface
from modules.auxiliar.repository.data_base.model import Auxiliar
from modules.auxiliar.dto import AuxiliarDTO
from datetime import datetime, time
import uuid as uuid


class AuxiliarRepository(AuxiliarRepositoryInterface):

    def _criar_auxiliar_objeto(self, auxiliar):
        return AuxiliarDTO(
            id = auxiliar.id,
            cpf = auxiliar.cpf,
            dia = auxiliar.procedimento,
            hora = auxiliar.vacina,
        )

    def criar_auxiliar(self, id: int,nome: str,cpf: str, endereco: str, num: str, cidade: str, contato: str, contato2: str, coren: str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_auxiliar = Auxiliar(id=id, nome=nome, cpf=cpf, endereco=endereco, num=num, cidade=cidade, contato=contato, contato2=contato2, coren=coren)
                db_connection.session.add(novo_auxiliar)
                db_connection.session.commit()
                return self._criar_auxiliar_objeto(novo_auxiliar)
        except Exception as exc:
            raise exc

    def buscar_auxiliar_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Auxiliar).filter(Auxiliar.id == id).one_or_none()
            data_resultado = self._criar_auxiliar_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_auxiliars(self):
        with DBConnectionHandler() as db_connection:
            list_auxiliars = []
            auxiliars = db_connection.session.query(Auxiliar).all()
            for auxiliar in auxiliars:
                list_auxiliars.append(
                    self._criar_auxiliar_objeto(auxiliar)
                )
            return list_auxiliars
        
    def atualizar_auxiliar(self, id: int,nome: str,cpf: str, endereco: str, num: str, cidade: str, contato: str, contato2: str, coren: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Auxiliar).filter(Auxiliar.id == id).one_or_none()
            if data:
                data.id = id
                data.nome = nome
                data.cpf = cpf
                data.endereco = endereco
                data.num = num
                data.cidade = cidade
                data.contato = contato
                data.contato2 = contato2
                data.coren = coren
                db_connection.session.commit()
                return self._criar_auxiliar_objeto(data)
            return None

    def deletar_auxiliar(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Auxiliar).filter(Auxiliar.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_auxiliar_objeto(data)
            return data