import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.medico.controller import MedicoController

api_atualizar_medico = Namespace("medico", description="Endpoint atualizar medico")


@api_atualizar_medico.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarMedico(Resource):

    def patch(self, id: int):
        data = api_atualizar_medico.payload
        try:
            response = MedicoController.atualizar_medico(data,id)
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