from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from modules.procedimento.repository.data_base.model import Procedimento
from modules.pagamento.repository.data_base.model import Pagamento
from modules.cirurgia.repository.data_base.model import Cirurgia
from modules.consulta.repository.data_base.model import Consulta
from modules.prontuario.repository.data_base.model import Prontuario


from infra.db.db_base import Base

class Paciente(Base):
    __tablename__ = "tb_paciente"
    
    #Campos
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    sexo = Column(String, nullable=False)
    dt_nasc = Column(DateTime, nullable=False)
    contato = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    cidade = Column(String,nullable=False)
    estado = Column(String, nullable=False)
    id_login = Column(Integer, ForeignKey('tb_login.id', ondelete="CASCADE", onupdate="CASCADE"))
    # Relacionamentos
    
    # fk_procedimento = relationship('Procedimento', back_populates='paciente')
    # fk_cirurgia = relationship('Cirurgia', back_populates='paciente')
    # fk_pagamento = relationship('Pagamento', back_populates='paciente')
    # fk_consulta = relationship('Consulta', back_populates='paciente')
    # fk_prontuario = relationship('Prontuario', back_populates='paciente')