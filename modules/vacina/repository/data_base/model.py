from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.orm import relationship
from modules.consulta.repository.data_base.model import Consulta

from infra.db.db_base import Base

class Vacina(Base):
    __tablename__ = "tb_vacina"
    
    #Campos
    nome = Column(String, nullable=False)
    proposito = Column(String, nullable=False)
    ml = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    vencimento = Column(DateTime, nullable=False)
     

    # Relacionamentos
    # fk_consulta = relationship('Consulta', back_populates='vacina')