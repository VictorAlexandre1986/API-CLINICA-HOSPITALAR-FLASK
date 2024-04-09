from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import relationship
from modules.procedimento.repository.data_base.model import Procedimento
from modules.medico.repository.data_base.model import Medico

from infra.db import Base

class Pagamento(Base):
    __tablename__ = "tb_pagamento"
    
    #Campos
    id_paciente = Column(ForeignKey('paciente.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_exame = Column(ForeignKey('exame.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_consulta = Column(ForeignKey('consula.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_cirurgia = Column(ForeignKey('cirurgia.id', ondelete="CASCADE", onupdate="CASCADE"))
    tipo_pagamento = Column(ForeignKey('tipo_pagamento.id', ondelete="CASCADE", onupdate="CASCADE"))
    numero_parcelas = Column(Integer,nullable=True)


    def __repr__(self):
        return f"Pagamento({self.id}, {self.id_paciente}, {self.id_exames}, {self.id_consulta}, {self.tipo_pagamento}, {self.numero_parcelas})"
