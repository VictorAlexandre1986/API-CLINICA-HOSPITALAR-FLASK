import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.procedimento.controller import ProcedimentoController

api_atualizar_procedimento = Namespace("procedimento", description="Endpoint atualizar procedimento")


@api_atualizar_procedimento.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarProcedimento(Resource):

    def patch(self, id: int):
        data = api_atualizar_procedimento.payload
        try:
            response = ProcedimentoController.atualizar_procedimento(data,id)
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