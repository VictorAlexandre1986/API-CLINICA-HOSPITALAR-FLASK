from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from modules.procedimento.repository.data_base.model import Procedimento
from modules.medico.repository.data_base.model import Medico
from modules.agenda.repository.data_base.model import Agenda

from infra.db import Base

class Cirurgia(Base):
    __tablename__ = "tb_cirurgia"
    
    #Campos
    id_medico = Column(Integer, ForeignKey('medico.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_paciente = Column(Integer, ForeignKey('paciente.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_procedimento = Column(Integer, ForeignKey('procedimento.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_auxiliar = Column(Integer, ForeignKey('auxiliar.id', ondelete="CASCADE", onupdate="CASCADE"))
    # Relacionamentos
    fk_agenda = relationship(Agenda, back_populates='cirurgia')
    
   