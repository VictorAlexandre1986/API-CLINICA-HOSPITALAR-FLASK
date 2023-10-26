from sqlalchemy import Column, Integer, String, DateTime, Time
from sqlalchemy.orm import relationship
from modules.procedimento.repository.data_base.model import Procedimento
from modules.medico.repository.data_base.model import Medico

from infra.db import Base

class Login(Base):
    __tablename__ = "tb_login"
    
    #Campos
    usuario = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    
    # Relacionamentos
    fk_procedimento = relationship(Procedimento, back_populates='agenda')
    fk_medico = relationship(Medico, back_populates='agenda')
    