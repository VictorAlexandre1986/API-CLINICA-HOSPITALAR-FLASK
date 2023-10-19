import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.prontuario.controller import ProntuarioController

api_criar_prontuario = Namespace("prontuario", description="Endpoint criar prontuario")


@api_criar_prontuario.route("/", methods=["POST"])
class CriarProntuario(Resource):

    def post(self):
        data = api_criar_prontuario.payload
        try:
            response = ProntuarioController.criar_prontuario(data)
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
         