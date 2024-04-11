from sqlalchemy import Column, Integer, String, DateTime, Time
from sqlalchemy.orm import relationship
from modules.paciente.repository.data_base.model import Paciente
from modules.medico.repository.data_base.model import Medico
from modules.auxiliar.repository.data_base.model import Auxiliar

from infra.db.db_base import Base

class Login(Base):
    __tablename__ = "tb_login"
    
    #Campos
    usuario = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    
    # Relacionamentos
    # fk_paciente = relationship('Paciente', back_populates='login')
    # fk_auxiliar = relationship('Auxiliar', back_populates='login')
    # fk_medico = relationship('Medico', back_populates='login')
    
    def __repr__(self):
        return f"Login(id={self.id}, usuario={self.usuario}, senha={self.senha})"