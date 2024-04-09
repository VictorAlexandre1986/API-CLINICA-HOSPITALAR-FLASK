from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from modules.consulta.repository.data_base.model import Consulta

from infra.db import Base

class Vacina(Base):
    __tablename__ = "tb_vacina"
    
    #Campos
    nome = Column(String, nullable=False)
    contra = Column(String, nullable=False)
    valor = Column(Float, nullable=False)

    # Relacionamentos
    fk_consulta = relationship(Consulta, back_populates='vacina')