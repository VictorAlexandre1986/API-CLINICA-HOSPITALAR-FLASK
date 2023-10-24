from sqlalchemy import Column, Integer, String, DateTime, Time
from sqlalchemy.orm import relationship
from modules.procedimento.repository.data_base.model import Procedimento
from modules.medico.repository.data_base.model import Medico

from infra.db import Base

class Agenda(Base):
    __tablename__ = "tb_agenda"
    
    #Campos
    cpf = Column(String, nullable=False)
    dia = Column(DateTime, nullable=False)
    hora = Column(Time, nullable=False)
    procedimento = Column(String, nullable=False)
    medico = Column(String,nullable=False)
    # Relacionamentos
    fk_procedimento = relationship(Procedimento, back_populates='agenda')
    fk_medico = relationship(Medico, back_populates='agenda')
    