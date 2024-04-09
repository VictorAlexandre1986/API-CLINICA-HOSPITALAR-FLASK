from flask import Blueprint, Flask
from flask_cors import CORS
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix


from application.rest.login.criar_login import api_criar_login
from application.rest.login.buscar_login import api_buscar_login
from application.rest.login.atualizar_login import api_atualizar_login
from application.rest.login.deletar_login import api_deletar_login

from application.rest.agenda.criar_agenda import api_criar_agenda
from application.rest.agenda.buscar_agenda import api_buscar_agenda
from application.rest.agenda.atualizar_agenda import api_atualizar_agenda
from application.rest.agenda.deletar_agenda import api_deletar_agenda

from application.rest.cirurgia.criar_cirurgia import api_criar_cirurgia
from application.rest.cirurgia.buscar_cirurgia import api_buscar_cirurgia
from application.rest.cirurgia.atualizar_cirurgia import api_atualizar_cirurgia
from application.rest.cirurgia.deletar_cirurgia import api_deletar_cirurgia

from application.rest.consulta.criar_consulta import api_criar_consulta
from application.rest.consulta.buscar_consulta import api_buscar_consulta
from application.rest.consulta.atualizar_consulta import api_atualizar_consulta
from application.rest.consulta.deletar_consulta import api_deletar_consulta

from application.rest.medico.criar_medico import api_criar_medico
from application.rest.medico.buscar_medico import api_buscar_medico
from application.rest.medico.atualizar_medico import api_atualizar_medico
from application.rest.medico.deletar_medico import api_deletar_medico

from application.rest.paciente.criar_paciente import api_criar_paciente
from application.rest.paciente.buscar_paciente import api_buscar_paciente
from application.rest.paciente.atualizar_paciente import api_atualizar_paciente
from application.rest.paciente.deletar_paciente import api_deletar_paciente

from application.rest.prontuario.criar_prontuario import api_criar_prontuario
from application.rest.prontuario.buscar_prontuario import api_buscar_prontuario
from application.rest.prontuario.atualizar_prontuario import api_atualizar_prontuario
from application.rest.prontuario.deletar_prontuario import api_deletar_prontuario

from application.rest.vacina.criar_vacina import api_criar_vacina
from application.rest.vacina.buscar_vacina import api_buscar_vacina
from application.rest.vacina.atualizar_vacina import api_atualizar_vacina
from application.rest.vacina.deletar_vacina import api_deletar_vacina

from application.rest.auxiliar.criar_auxiliar import api_criar_auxiliar
from application.rest.auxiliar.buscar_auxiliar import api_buscar_auxiliar
from application.rest.auxiliar.atualizar_auxiliar import api_atualizar_auxiliar
from application.rest.auxiliar.deletar_auxiliar import api_deletar_auxiliar

from application.rest.procedimento.criar_procedimento import api_criar_procedimento
from application.rest.procedimento.buscar_procedimento import api_buscar_procedimento
from application.rest.procedimento.atualizar_procedimento import api_atualizar_procedimento
from application.rest.procedimento.deletar_procedimento import api_deletar_procedimento

from application.rest.pagamento.criar_pagamento import api_criar_pagamento
from application.rest.pagamento.buscar_pagamento import api_buscar_pagamento
from application.rest.pagamento.atualizar_pagamento import api_atualizar_pagamento
from application.rest.pagamento.deletar_pagamento import api_deletar_pagamento

from application.rest.exame.criar_exame import api_criar_exame
from application.rest.exame.buscar_exame import api_buscar_exame
from application.rest.exame.atualizar_exame import api_atualizar_exame
from application.rest.exame.deletar_exame import api_deletar_exame


class ServeApplication:

    def __init__(self):
        self.app = Flask(__name__)
        self._blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

    def _init_blueprints(self, app):
        api = Api(
            self._blueprint,
            title="Clinica",
            version="0.0.1",
            doc="/docs",
        )

        api.add_namesppace(api_criar_login)
        api.add_namespace(api_buscar_login)
        api.add_namespace(api_atualizar_login)
        api.add_namespace(api_deletar_login)
        
        api.add_namespace(api_criar_agenda)
        api.add_namespace(api_buscar_agenda)
        api.add_namespace(api_atualizar_agenda)
        api.add_namespace(api_deletar_agenda)
        
        api.add_namespace(api_criar_cirurgia)
        api.add_namespace(api_buscar_cirurgia)
        api.add_namespace(api_atualizar_cirurgia)
        api.add_namespace(api_deletar_cirurgia)
        
        api.add_namespace(api_criar_consulta)
        api.add_namespace(api_buscar_consulta)
        api.add_namespace(api_atualizar_consulta)
        api.add_namespace(api_deletar_consulta)
        
        api.add_namespace(api_criar_medico)
        api.add_namespace(api_buscar_medico)
        api.add_namespace(api_atualizar_medico)
        api.add_namespace(api_deletar_medico)
        
        api.add_namespace(api_criar_paciente)
        api.add_namespace(api_buscar_paciente)
        api.add_namespace(api_atualizar_paciente)
        api.add_namespace(api_deletar_paciente)

        api.add_namespace(api_criar_prontuario)
        api.add_namespace(api_buscar_prontuario)
        api.add_namespace(api_atualizar_prontuario)
        api.add_namespace(api_deletar_prontuario)
        
        api.add_namespace(api_criar_vacina)
        api.add_namespace(api_buscar_vacina)
        api.add_namespace(api_atualizar_vacina)
        api.add_namespace(api_deletar_vacina)

        api.add_namespace(api_criar_auxiliar)
        api.add_namespace(api_buscar_auxiliar)
        api.add_namespace(api_atualizar_auxiliar)
        api.add_namespace(api_deletar_auxiliar)
        
        api.add_namespace(api_criar_procedimento)
        api.add_namespace(api_buscar_procedimento)
        api.add_namespace(api_atualizar_procedimento)
        api.add_namespace(api_deletar_procedimento)
        
        api.add_namespace(api_criar_exame)
        api.add_namespace(api_buscar_exame)
        api.add_namespace(api_atualizar_exame)
        api.add_namespace(api_deletar_exame)




        
        app.register_blueprint(self._blueprint)

    def create_app(self):
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

        self._init_blueprints(self.app)
        CORS(self.app)

        return self.app


app = ServeApplication().create_app()