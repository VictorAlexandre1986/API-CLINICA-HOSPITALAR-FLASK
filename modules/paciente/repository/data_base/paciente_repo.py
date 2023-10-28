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
            endereco = paciente.endereco,
            num = paciente.num,
            bairro = paciente.bairro,
            cidade = paciente.cidade,
            contato = paciente.contato,
            contato2= paciente.contato2,
            email = paciente.email
        )

    def criar_paciente(self, id: int, nome: str, cpf: str, sexo:str, endereco: str, num: str, bairro: str, cidade: str, contato: str, contato2: str, email: str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_paciente = Paciente(id=id, nome=nome, cpf=cpf, sexo=sexo, endereco=endereco, num=num, bairro=bairro, cidade=cidade, contato=contato, contato2=contato2, email=email)
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
        
    def atualizar_paciente(self, id: int, nome: str, cpf: str, sexo:str, endereco: str, num: str, bairro: str, cidade: str, contato: str, contato2: str, email: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Paciente).filter(Paciente.id == id).one_or_none()
            if data:
                data.id = id
                data.nome = nome
                data.cpf = cpf
                data.sexo = sexo
                data.endereco = endereco
                data.num = num
                data.bairro = bairro
                data.cidade = cidade
                data.contato = contato
                data.contato2 = contato2
                data.email = email
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
        