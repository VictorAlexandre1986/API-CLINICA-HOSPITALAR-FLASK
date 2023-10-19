import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.paciente.controller import PacienteController

api_buscar_paciente = Namespace("paciente", description="Endpoint buscar paciente")


@api_buscar_paciente.route("/<int:id>", methods=["GET"])
class BuscarPacientePorId(Resource):

    def get(self, id: int):
        try:
            response = PacienteController.buscar_paciente_por_id(id)
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
            return Response(
                json.dumps({"msg": 'Bad request'}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )


@api_buscar_paciente.route("/", methods=["GET"])
class BuscarPacientes(Resource):

    def get(self):
        try:
            response = PacienteController.buscar_pacientes()
            return Response(
                json.dumps(response),
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
            return Response(
                json.dumps({"msg": 'Bad request'}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )