import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.paciente.controller import PacienteController

api_deletar_paciente = Namespace("paciente", description="Endpoint deletar paciente")


@api_deletar_paciente.route("/<int:id>", methods=["DELETE"])
class DeletarPaciente(Resource):

    def delete(self, id: int):
        try:
            PacienteController.deletar_paciente(id)
            return Response(
                json.dumps({"msg": "Excluído com sucesso."}),
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