import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.paciente.controller import PacienteController

api_atualizar_paciente = Namespace("paciente", description="Endpoint atualizar paciente")


@api_atualizar_paciente.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarPaciente(Resource):

    def patch(self, id: int):
        data = api_atualizar_paciente.payload
        try:
            response = PacienteController.atualizar_paciente(data,id)
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