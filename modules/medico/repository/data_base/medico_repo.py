from infra.db.db_config import DBConnectionHandler
from modules.medico.repository.data_base.interface import MedicoRepositoryInterface
from modules.medico.repository.data_base.model import Medico
from modules.medico.dto import MedicoDTO
from datetime import datetime, time
import uuid as uuid


class MedicoRepository(MedicoRepositoryInterface):

    def _criar_medico_objeto(self, medico):
        return MedicoDTO(
            id = medico.id,
            nome = medico.nome,
            crm = medico.crm,
            especialidade = medico.especialidade,
            contato = medico.contato,
            id_login = medico.id_login
        )

    def criar_medico(self, id: int, nome: str, crm: str, especialidade:str, contato:str, id_login: int):
        try:
            with DBConnectionHandler() as db_connection:
                novo_medico = Medico(id=id, nome=nome, crm=crm, especialidade=especialidade, contato=contato, id_login=id_login)
                db_connection.session.add(novo_medico)
                db_connection.session.commit()
                return self._criar_medico_objeto(novo_medico)
        except Exception as exc:
            raise exc

    def buscar_medico_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Medico).filter(Medico.id == id).one_or_none()
            data_resultado = self._criar_medico_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_medicos(self):
        with DBConnectionHandler() as db_connection:
            list_medicos = []
            medicos = db_connection.session.query(Medico).all()
            for medico in medicos:
                list_medicos.append(
                    self._criar_medico_objeto(medico)
                )
            return list_medicos
        
    def atualizar_medico(self, id: int, nome: str, crm: str, especialidade:str, contato:str, id_login: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Medico).filter(Medico.id == id).one_or_none()
            if data:
                data.id = id
                data.nome = nome
                data.crm = crm
                data.especialidade = especialidade
                data.contato = contato
                data.id_login = id_login
                db_connection.session.commit()
                return self._criar_medico_objeto(data)
            return None

    def deletar_medico(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Medico).filter(Medico.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_medico_objeto(data)
            return data