from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from modules.cirurgia.repository.data_base.model import Cirurgia

from infra.db import Base

class Auxiliar(Base):
    __tablename__ = "tb_auxiliar"
    
    #Campos
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    funcao = Column(String, nullable=False)
    contato = Column(String, nullable=False)
    credencial = Column(String, nullable=True)
    id_login = Column(ForeignKey('login.id',ondelete="CASCADE", onupdate="CASCADE"))
    
    # Relacionamentos
    fk_cirurgia = relationship(Cirurgia, back_populates='auxiliar')