import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.prontuario.controller import ProntuarioController

api_atualizar_prontuario = Namespace("prontuario", description="Endpoint atualizar prontuario")


@api_atualizar_prontuario.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarProntuario(Resource):

    def patch(self, id: int):
        data = api_atualizar_prontuario.payload
        try:
            response = ProntuarioController.atualizar_prontuario(data,id)
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