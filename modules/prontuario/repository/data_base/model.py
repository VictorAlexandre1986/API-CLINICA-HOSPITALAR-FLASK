from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from modules.procedimento.repository.data_base.model import Procedimento
from modules.consulta.repository.data_base.model import Consulta

from infra.db import Base

class Prontuario(Base):
    __tablename__ = "tb_prontuario"
    
    #Campos
    prontuario = Column(String, nullable=False)
    # Relacionamentos
    id_paciente = Column(ForeignKey('paciente.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_medico = Column(ForeignKey('medico.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_procedimento = Column(ForeignKey('procedimento.id', ondelete="CASCADE", onupdate="CASCADE"))
    fk_consulta = relationship(Consulta, back_populates='prontuario')