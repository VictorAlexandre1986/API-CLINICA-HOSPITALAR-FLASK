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
            crm = medico.crm,
            especialidade = medico.especialidade,
            contato = medico.contato,
            contato2 = medico.contato2,
            sexo = medico.sexo,
            endereco = medico.endereco,
            num = medico.num,
            bairro = medico.bairro,
            cidade = medico.cidade,
        )

    def criar_medico(self, id: int, crm: str, especialidade:str, contato:str, contato2:str, sexo:str, endereco:str, num:str, bairro: str, cidade: str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_medico = Medico(id=id, crm=crm, especialidade=especialidade, contato=contato, contato2=contato2, sexo=sexo, endereco=endereco, num=num, bairro=bairro, cidade=cidade)
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
        
    def atualizar_medico(self, id: int, crm: str, especialidade:str, contato:str, contato2:str, sexo:str, endereco:str, num:str, bairro: str, cidade: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Medico).filter(Medico.id == id).one_or_none()
            if data:
                data.id = id
                data.crm = crm
                data.especialidade = especialidade
                data.contato = contato
                data.contato2 = contato2
                data.sexo = sexo
                data.endereco = endereco
                data.num = num
                data.bairro = bairro
                data.cidade = cidade
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