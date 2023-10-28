from infra.db.db_config import DBConnectionHandler
from modules.agenda.repository.data_base.interface import AgendaRepositoryInterface
from modules.agenda.repository.data_base.model import Agenda
from modules.agenda.dto import AgendaDTO
from datetime import datetime, time
import uuid as uuid


class AgendaRepository(AgendaRepositoryInterface):

    def _criar_agenda_objeto(self, agenda):
        return AgendaDTO(
            id = agenda.id,
            cpf = agenda.cpf,
            dia = agenda.dia,
            hora = agenda.hora,
            procedimento = agenda.procedimento,
            medico = agenda.medico
        )

    def criar_agenda(self, id: int, cpf: str, dia:datetime, hora:time, procedimento:str, medico:str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_agenda = Agenda(id=id, cpf=cpf, dia=dia, hora=hora, procedimento=procedimento, medico=medico)
                db_connection.session.add(novo_agenda)
                db_connection.session.commit()
                return self._criar_agenda_objeto(novo_agenda)
        except Exception as exc:
            raise exc

    def buscar_agenda_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Agenda).filter(Agenda.id == id).one_or_none()
            data_resultado = self._criar_agenda_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_agendas(self):
        with DBConnectionHandler() as db_connection:
            list_agendas = []
            agendas = db_connection.session.query(Agenda).all()
            for agenda in agendas:
                list_agendas.append(
                    self._criar_agenda_objeto(agenda)
                )
            return list_agendas
        
    def atualizar_agenda(self, id: int, cpf: str, dia:datetime, hora:time, procedimento:str, medico:str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Agenda).filter(Agenda.id == id).one_or_none()
            if data:
                data.id = id
                data.cpf = cpf
                data.dia = dia
                data.hora = hora
                data.procedimento = procedimento
                data.medico = medico
                db_connection.session.commit()
                return self._criar_agenda_objeto(data)
            return None

    def deletar_agenda(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Agenda).filter(Agenda.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_agenda_objeto(data)
            return data