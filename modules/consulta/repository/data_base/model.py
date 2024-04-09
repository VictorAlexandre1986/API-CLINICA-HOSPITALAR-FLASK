from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from modules.pagamento.repository.data_base.model import Pagamento

from infra.db import Base

class Consulta(Base):
    __tablename__ = "tb_consulta"
    
    #Campos
    id_paciente = Column(ForeignKey('paciente.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_agenda = Column(ForeignKey('agenda.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_medico = Column(ForeignKey('medico.id', onupdate="CASCADE", onupdate="CASCADE"))
    id_prontuario =Column (ForeignKey('prontuario.id', onupdate="CASCADE", onupdate="CASCADE"))
    id_procedimento = Column(ForeignKey('procedimento.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_exame = Column(ForeignKey('exame.id', onupdate="CASCADE", onupdate="CASCADE"))
    id_vacina = Column(ForeignKey('vacina.id', onupdate="CASCADE", onupdate="CASCADE"))
    
    
    # Relacionamentos
    fk_pagamento = relationship(Pagamento, back_populates='consulta')
    
    def __repr__(self):
        return f"Consulta({self.id}, {self.id_paciente}, {self.id_agenda}, {self.id_medico}, {self.id_prontuario}, {self.id_procedimento}, {self.id_exame}, {self.id_vacina})"
    