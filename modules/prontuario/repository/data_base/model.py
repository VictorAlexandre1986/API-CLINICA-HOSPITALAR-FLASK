from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modules.consulta.repository.data_base.model import Consulta
from modules.consulta.repository.data_base.model import Consulta

from infra.db.db_base import Base

class Prontuario(Base):
    __tablename__ = "tb_prontuario"
    
    #Campos
    prontuario = Column(String, nullable=False)
    # Relacionamentos
    id_paciente = Column(Integer, ForeignKey('tb_paciente.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_medico = Column(Integer, ForeignKey('tb_medico.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_procedimento = Column(Integer, ForeignKey('tb_procedimento.id', ondelete="CASCADE", onupdate="CASCADE"))
    # fk_consulta = relationship('Consulta', back_populates='prontuario')
