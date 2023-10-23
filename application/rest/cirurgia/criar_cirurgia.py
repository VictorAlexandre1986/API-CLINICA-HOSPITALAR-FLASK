import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.cirurgia.controller import CirurgiaController

api_criar_cirurgia = Namespace("cirurgia", description="Endpoint criar cirurgia")


@api_criar_cirurgia.route("/", methods=["POST"])
class CriarCirurgia(Resource):

    def post(self):
        data = api_criar_cirurgia.payload
        try:
            response = CirurgiaController.criar_cirurgia(data)
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