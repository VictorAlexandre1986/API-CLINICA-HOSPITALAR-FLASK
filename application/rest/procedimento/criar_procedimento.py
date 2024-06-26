import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.procedimento.controller import ProcedimentoController

api_criar_procedimento = Namespace("procedimento", description="Endpoint procedimento")


@api_criar_procedimento.route("/", methods=["POST"])
class CriarProcedimento(Resource):

    def post(self):
        data = api_criar_procedimento.payload
        try:
            response = ProcedimentoController.criar_procedimento(data)
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