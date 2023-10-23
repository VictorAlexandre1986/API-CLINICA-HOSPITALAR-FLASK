import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.cirurgia.controller import CirurgiaController

api_atualizar_cirurgia = Namespace("cirurgia", description="Endpoint atualizar cirurgia")


@api_atualizar_cirurgia.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarCirurgia(Resource):

    def patch(self, id: int):
        data = api_atualizar_cirurgia.payload
        try:
            response = CirurgiaController.atualizar_agenda(data,id)
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