from infra.db.db_config import DBConnectionHandler
from modules.prontuario.repository.data_base.interface import ProntuarioRepositoryInterface
from modules.prontuario.repository.data_base.model import Prontuario
from modules.prontuario.dto import ProntuarioDTO
from datetime import datetime, time
import uuid as uuid


class ProntuarioRepository(ProntuarioRepositoryInterface):

    def _criar_prontuario_objeto(self, prontuario):
        return ProntuarioDTO(
            id = prontuario.id,
            cpf = prontuario.cpf,
            dia = prontuario.procedimento,
            hora = prontuario.vacina,
        )

    def criar_prontuario(self, id: int, cpf: str, procedimento: int, vacina: int):
        try:
            with DBConnectionHandler() as db_connection:
                novo_prontuario = Prontuario(id=id, cpf=cpf, procedimento=procedimento, vacina=vacina)
                db_connection.session.add(novo_prontuario)
                db_connection.session.commit()
                return self._criar_prontuario_objeto(novo_prontuario)
        except Exception as exc:
            raise exc

    def buscar_prontuario_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Prontuario).filter(Prontuario.id == id).one_or_none()
            data_resultado = self._criar_prontuario_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_prontuarios(self):
        with DBConnectionHandler() as db_connection:
            list_prontuarios = []
            prontuarios = db_connection.session.query(Prontuario).all()
            for prontuario in prontuarios:
                list_prontuarios.append(
                    self._criar_prontuario_objeto(prontuario)
                )
            return list_prontuarios
        
    def atualizar_prontuario(self, id: int, cpf: str, procedimento:str, vacina: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Prontuario).filter(Prontuario.id == id).one_or_none()
            if data:
                data.id = id
                data.cpf = cpf
                data.procedimento = procedimento
                data.vacina = vacina
                db_connection.session.commit()
                return self._criar_prontuario_objeto(data)
            return None

    def deletar_prontuario(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Prontuario).filter(Prontuario.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_prontuario_objeto(data)
            return data