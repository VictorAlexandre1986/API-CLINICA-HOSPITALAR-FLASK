import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.exame.controller import ExameController

api_deletar_exame = Namespace("exame", description="Endpoint deletar exame")


@api_deletar_exame.route("/<int:id>", methods=["DELETE"])
class DeletarExame(Resource):

    def delete(self, id: int):
        try:
            ExameController.deletar_exame(id)
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