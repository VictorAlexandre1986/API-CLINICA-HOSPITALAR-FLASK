from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from modules.agenda.repository.data_base.model import Agenda



from infra.db.db_base import Base

class Cirurgia(Base):
    __tablename__ = "tb_cirurgia"
    
    #Campos
    id_medico = Column(Integer, ForeignKey('tb_medico.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_paciente = Column(Integer, ForeignKey('tb_paciente.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_procedimento = Column(Integer, ForeignKey('tb_procedimento.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_auxiliar = Column(Integer, ForeignKey('tb_auxiliar.id', ondelete="CASCADE", onupdate="CASCADE"))
    # Relacionamentos
    # fk_agenda = relationship('Agenda', back_populates='cirurgia')

    
   