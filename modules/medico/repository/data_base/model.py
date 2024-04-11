from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from modules.procedimento.repository.data_base.model import Procedimento
from modules.agenda.repository.data_base.model import Agenda
from modules.cirurgia.repository.data_base.model import Cirurgia
from modules.consulta.repository.data_base.model import Consulta
from modules.prontuario.repository.data_base.model import Prontuario




from infra.db.db_base import Base

class Medico(Base):
    __tablename__ = "tb_medico"
    
    #Campos
    nome = Column(String, nullable=False)
    crm = Column(String, nullable=False)
    contato = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)
    id_login = Column(ForeignKey('tb_login.id', ondelete="CASCADE", onupdate="CASCADE"))

    # Relacionamentos
    # fk_procedimento = relationship('Procedimento', back_populates='medico')
    # fk_agenda = relationship('Agenda', back_populates='medico')
    # fk_cirurgia = relationship('Cirurgia', back_populates='medico')
    # fk_consulta = relationship('Consulta', back_populates='medico')
    # fk_prontuario = relationship('Prontuario', back_populates='medico')

    