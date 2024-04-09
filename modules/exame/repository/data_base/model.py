from sqlalchemy import Column, Float, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from modules.pagamento.repository.data_base.model import Pagamento
from modules.consulta.repository.data_base.model import Consulta

from infra.db import Base

class Exame(Base):
    __tablename__ = "tb_exame"
    
    #Campos
    tipo_exame = Column(String,nullable=False)
    valor =Column(Float, nullable=False)
    exame = Column(ForeignKey('exame.id', ondelete="CASCADE", onupdate="CASCADE"))
    # Relacionamentos
    fk_pagamento = relationship(Pagamento, back_populates='exame')
    fk_consulta = relationship(Consulta, back_populates='exame')
    