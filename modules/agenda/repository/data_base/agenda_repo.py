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
            id_procedimento = agenda.procedimento,
            id_medico = agenda.medico,
            id_cirurgia = agenda.id_cirurgia
        )

    def criar_agenda(self, id: int, cpf: str, dia:datetime, id_procedimento: int, id_medico: int, id_cirurgia: int):
        try:
            with DBConnectionHandler() as db_connection:
                novo_agenda = Agenda(id=id, cpf=cpf, dia=dia, id_procedimento=id_procedimento, id_medico=id_medico, id_cirurgia=id_cirurgia)
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
        
    def atualizar_agenda(self, id: int, cpf: str, dia:datetime, id_procedimento:int, id_medico:int, id_cirurgia:int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Agenda).filter(Agenda.id == id).one_or_none()
            if data:
                data.id = id
                data.cpf = cpf
                data.dia = dia
                data.id_procedimento = id_procedimento
                data.id_medico = id_medico
                data.id_cirurgia = id_cirurgia
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