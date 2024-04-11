from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


from infra.db.db_base import Base

class Pagamento(Base):
    __tablename__ = "tb_pagamento"
    
    #Campos
    id_paciente = Column(Integer,ForeignKey('tb_paciente.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_exame = Column(Integer,ForeignKey('tb_exame.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_consulta = Column(Integer,ForeignKey('tb_consulta.id', ondelete="CASCADE", onupdate="CASCADE"))
    id_cirurgia = Column(Integer,ForeignKey('tb_cirurgia.id', ondelete="CASCADE", onupdate="CASCADE"))
    numero_parcelas = Column(Integer,nullable=True)


    def __repr__(self):
        return f"Pagamento({self.id}, {self.id_paciente}, {self.id_exames}, {self.id_consulta}, {self.tipo_pagamento}, {self.numero_parcelas})"
