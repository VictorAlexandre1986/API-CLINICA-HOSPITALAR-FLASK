from infra.db.db_config import DBConnectionHandler
from modules.paciente.repository.data_base.interface import PacienteRepositoryInterface
from modules.paciente.repository.data_base.model import Paciente
from modules.paciente.dto import PacienteDTO
from datetime import datetime, time
import uuid as uuid


class PacienteRepository(PacienteRepositoryInterface):

    def _criar_paciente_objeto(self, paciente):
        return PacienteDTO(
            id = paciente.id,
            nome = paciente.nome,
            cpf = paciente.cpf,
            sexo = paciente.sexo,
            dt_nasc = paciente.dt_nasc,
            endereco = paciente.endereco,
            bairro = paciente.bairro,
            cidade = paciente.cidade,
            estado = paciente.estado,
            contato= paciente.contato,
            id_login = paciente.id_login
        )

    def criar_paciente(self, id: int, nome: str, cpf: str, sexo:str, dt_nasc: datetime, endereco: str, bairro: str, cidade: str, contato: str, estado: str, id_login: int):
        try:
            with DBConnectionHandler() as db_connection:
                # dt_nasc = datetime.strptime(dt_nasc, "%Y-%m-%d %H:%M:%S")
                novo_paciente = Paciente(id=id, nome=nome, cpf=cpf, sexo=sexo, dt_nasc=dt_nasc, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, contato=contato, id_login=id_login)
                db_connection.session.add(novo_paciente)
                db_connection.session.commit()
                return self._criar_paciente_objeto(novo_paciente)
        except Exception as exc:
            raise exc

    def buscar_paciente_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Paciente).filter(Paciente.id == id).one_or_none()
            data_resultado = self._criar_paciente_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_pacientes(self):
        with DBConnectionHandler() as db_connection:
            list_pacientes = []
            pacientes = db_connection.session.query(Paciente).all()
            for paciente in pacientes:
                list_pacientes.append(
                    self._criar_paciente_objeto(paciente)
                )
            return list_pacientes
        
    def atualizar_paciente(self, id: int, nome: str, cpf: str, sexo:str, dt_nasc: datetime, endereco: str, bairro: str, cidade: str, estado: str, contato: str, id_login:int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Paciente).filter(Paciente.id == id).one_or_none()
            # dt_nasc = datetime.strptime(data.dt_nasc, "%Y-%m-%d %H:%M:%S")
            if data:
                data.id = id
                data.nome = nome
                data.cpf = cpf
                data.sexo = sexo
                data.dt_nasc = dt_nasc
                data.endereco = endereco
                data.bairro = bairro
                data.cidade = cidade
                data.estado = estado
                data.contato = contato
                data.id_login = id_login
                db_connection.session.commit()
                return self._criar_paciente_objeto(data)
            return None

    def deletar_paciente(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Paciente).filter(Paciente.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_paciente_objeto(data)
            return data
        