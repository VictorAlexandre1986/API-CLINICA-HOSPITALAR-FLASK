from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modules.pagamento.repository.data_base.model import Pagamento


from infra.db.db_base import Base

class Consulta(Base):
    __tablename__ = "tb_consulta"
    
    #Campos
    id_paciente = Column(Integer, ForeignKey('tb_paciente.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_agenda = Column(Integer, ForeignKey('tb_agenda.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_medico = Column(Integer, ForeignKey('tb_medico.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_prontuario =Column (Integer, ForeignKey('tb_prontuario.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_procedimento = Column(Integer, ForeignKey('tb_procedimento.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_exame = Column(Integer, ForeignKey('tb_exame.id', onupdate="CASCADE", ondelete="CASCADE"))
    id_vacina = Column(Integer, ForeignKey('tb_vacina.id', onupdate="CASCADE", ondelete="CASCADE"))
    
    
    # Relacionamentos
    # fk_pagamento = relationship('Pagamento', back_populates='consulta')

    
    def __repr__(self):
        return f"Consulta({self.id}, {self.id_paciente}, {self.id_agenda}, {self.id_medico}, {self.id_prontuario}, {self.id_procedimento}, {self.id_exame}, {self.id_vacina})"
    