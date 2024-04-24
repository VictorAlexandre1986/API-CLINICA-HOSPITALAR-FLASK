import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.paciente.controller import PacienteController

api_criar_paciente = Namespace("paciente", description="Endpoint paciente")


@api_criar_paciente.route("/", methods=["POST"])
class CriarPaciente(Resource):

    def post(self):
        data = api_criar_paciente.payload
        try:
            response = PacienteController.criar_paciente(data)
            return Response(
                response.json(),
                mimetype="application/json",
                status=200,
            )

        except ValidationError as exc:
            return Response(
                exc.json(),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )
          
            

        except ValueError as exc:
            return Response(
                json.dumps({'msg': exc.args[0]}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )

        except Exception as exc:
            print(exc)
            return Response(
                json.dumps({"msg": 'Bad request'}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )