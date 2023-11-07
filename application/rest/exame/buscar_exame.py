import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.exame.controller import ExameController

api_buscar_exame = Namespace("exame", description="Endpoint buscar exame")


@api_buscar_exame.route("/<int:id>", methods=["GET"])
class BuscarExamePorId(Resource):

    def get(self, id: int):
        try:
            response = ExameController.buscar_exame_por_id(id)
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


@api_buscar_exame.route("/", methods=["GET"])
class BuscarExames(Resource):

    def get(self):
        try:
            response = ExameController.buscar_exames()
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