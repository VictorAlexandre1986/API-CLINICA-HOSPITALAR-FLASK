import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.vacina.controller import VacinaController

api_buscar_vacina = Namespace("vacina", description="Endpoint buscar vacina")


@api_buscar_vacina.route("/<int:id>", methods=["GET"])
class BuscarVacinaPorId(Resource):

    def get(self, id: int):
        try:
            response = VacinaController.buscar_vacina_por_id(id)
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


@api_buscar_vacina.route("/", methods=["GET"])
class BuscarVacinas(Resource):

    def get(self):
        try:
            response = VacinaController.buscar_vacinas()
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
            print(exc)
            # return Response(
            #     json.dumps({"msg": 'Bad request'}),
            #     mimetype="application/json",
            #     status=HTTPStatus.BAD_REQUEST
            # )