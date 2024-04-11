from sqlalchemy import Column, Integer, String, DateTime, Time, Float, ForeignKey
from sqlalchemy.orm import relationship
from modules.consulta.repository.data_base.model import Consulta
from modules.agenda.repository.data_base.model import Agenda
from modules.prontuario.repository.data_base.model import Prontuario


from infra.db.db_base import Base

class Procedimento(Base):
    __tablename__ = "tb_procedimento"
    
    #Campos
    procedimento = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    id_medico = Column(Integer, ForeignKey('tb_medico.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_paciente = Column(Integer, ForeignKey('tb_paciente.id', ondelete="CASCADE", onupdate="CASCADE"))
    # Relacionamentos
    # fk_agenda = relationship('Agenda', back_populates='procedimento')
    # fk_consulta = relationship('Consulta', back_populates='procedimento')
    # fk_prontuario = relationship('Prontuario', back_populates='procedimento')
 
    
    def __repr__(self):
        return f"Procedimento({self.id}, {self.procedimento}, {self.valor}, {self.id_medico}, {self.id_paciente})"