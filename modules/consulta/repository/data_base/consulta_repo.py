from infra.db.db_config import DBConnectionHandler
from modules.consulta.repository.data_base.interface import ConsultaRepositoryInterface
from modules.consulta.repository.data_base.model import Consulta
from modules.consulta.dto import ConsultaDTO
from datetime import datetime, time
import uuid as uuid


class ConsultaRepository(ConsultaRepositoryInterface):

    def _criar_consulta_objeto(self, consulta):
        return ConsultaDTO(
            id = consulta.id,
            data = consulta.data,
            hora = consulta.hora,
            procedimento = consulta.procedimento,
            exame = consulta.exame,
            vacina = consulta.vacina,
            medico = consulta.medico,
            auxiliar = consulta.auxiliar
        )

    def criar_consulta(self, id: int, data: datetime, hora: time, procedimento: str, exame: str, vacina: str, medico: str, auxiliar: str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_consulta = Consulta(id = id, data = data, hora = hora, procedimento = procedimento, exame = exame, vacina = vacina, medico = medico, auxiliar = auxiliar)
                db_connection.session.add(novo_consulta)
                db_connection.session.commit()
                return self._criar_consulta_objeto(novo_consulta)
        except Exception as exc:
            raise exc

    def buscar_consulta_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Consulta).filter(Consulta.id == id).one_or_none()
            data_resultado = self._criar_consulta_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_consultas(self):
        with DBConnectionHandler() as db_connection:
            list_consultas = []
            consultas = db_connection.session.query(Consulta).all()
            for consulta in consultas:
                list_consultas.append(
                    self._criar_consulta_objeto(consulta)
                )
            return list_consultas
        
    def atualizar_consulta(self, id: int, data: datetime, hora: time, procedimento: str, exame: str, vacina: str, medico: str, auxiliar: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Consulta).filter(Consulta.id == id).one_or_none()
            if data:
                data.id = id
                data.data = data
                data.hora = hora
                data.procedimento = procedimento
                data.exame = exame
                data.vacina = vacina
                data.medico = medico
                data.auxiliar = auxiliar
                db_connection.session.commit()
                return self._criar_consulta_objeto(data)
            return None

    def deletar_consulta(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Consulta).filter(Consulta.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_consulta_objeto(data)
            return data