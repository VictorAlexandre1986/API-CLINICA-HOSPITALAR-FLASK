from infra.db.db_config import DBConnectionHandler
from modules.procedimento.repository.data_base.interface import ProcedimentoRepositoryInterface
from modules.procedimento.repository.data_base.model import Procedimento
from modules.procedimento.entity import ProcedimentoEntity
from datetime import datetime, time
import uuid as uuid


class ProcedimentoRepository(ProcedimentoRepositoryInterface):

    def _criar_procedimento_objeto(self, procedimento):
        return ProcedimentoEntity(
            id = procedimento.id,
            procedimento = procedimento.procedimento,
            id_exame = procedimento.id_exame,
            id_vacina = procedimento.id_vacina,
            id_cirurgia = procedimento.id_cirurgia,
            id_medico = procedimento.id_medico,
            id_paciente = procedimento.id_paciente,
            id_auxiliar = procedimento.id_auxiliar
        )

    def criar_procedimento(self, id: int, procedimento: str, id_exame: int, id_vacina: int, id_cirurgia: int, id_medico: int, id_paciente: int, id_auxiliar: int):
        try:
            with DBConnectionHandler() as db_connection:
                novo_procedimento = Procedimento(id=id, procedimento = procedimento, id_exame = id_exame, id_vacina=id_vacina, id_cirurgia=id_cicrugia, id_medico=id_medico, id_paciente=id_paciente, id_auxiliar=id_auxiliar)
                db_connection.session.add(novo_procedimento)
                db_connection.session.commit()
                return self._criar_procedimento_objeto(novo_procedimento)
        except Exception as exc:
            raise exc

    def buscar_procedimento_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Procedimento).filter(Procedimento.id == id).one_or_none()
            data_resultado = self._criar_procedimento_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_procedimento_por_id_paciente(self, id_paciente: int):
        with DBConnectionHandler() as db_connection:
            list_procedimentos = []
            procedimentos = db_connection.session.query(Procedimento).filter(Procedimento.id_paciente == id_paciente).one_or_none()
            for procedimento in procedimentos:
                list_procedimentos.append(
                    self._criar_procedimento_objeto(procedimento)
                )
            return list_procedimentos

    def buscar_procedimentos(self):
        with DBConnectionHandler() as db_connection:
            list_procedimentos = []
            procedimentos = db_connection.session.query(Procedimento).all()
            for procedimento in procedimentos:
                list_procedimentos.append(
                    self._criar_procedimento_objeto(procedimento)
                )
            return list_procedimentos
        
    def atualizar_procedimento(self, id: int, procedimento: str, id_exame: int, id_vacina: int, id_cirurgia: int, id_medico: int, id_paciente: int, id_auxiliar: int ):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Procedimento).filter(Procedimento.id == id).one_or_none()
            if data:
                data.id = id
                data.procedimento = procedimento
                data.id_exame = id_exame
                data.id_vacina = id_vacina
                data.id_cirurgia = id_cirurgia
                data.id_medico = id_medico
                data.id_paciente = id_paciente
                data.id_auxiliar = id_auxiliar
                db_connection.session.commit()
                return self._criar_procedimento_objeto(data)
            return None

    def deletar_procedimento(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Procedimento).filter(Procedimento.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_procedimento_objeto(data)
            return data