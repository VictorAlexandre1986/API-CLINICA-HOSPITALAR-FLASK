from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from modules.consulta.repository.data_base.model import Consulta



from infra.db import Base

class Agenda(Base):
    __tablename__ = "tb_agenda"
    
    #Campos
    cpf = Column(String, nullable=False)
    dia = Column(DateTime, nullable=False)

    id_medico = Column(Integer, ForeignKey('medico.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_procedimento = Column(Integer, ForeignKey('procedimento.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_cirurgia = Column(Integer, ForeignKey('cirurgia.id', ondelete="CASCADE", onupdate="CASCADE"))
    
    fk_consulta = relationship(Consulta, back_populates='agenda')

    def __repr__(self):
        return f"Agenda({self.id}, {self.dia}, {self.cpf}, {self.id_procedimento}, {self.id_medico}, {self.id_cirurgia})"