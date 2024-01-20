from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
import jwt
from .auth_jwt import token_creator, token_verify

route_bp = Blueprint('route', __name__)


@route_bp.route("/secret", methods=["GET"])
@token_verify 
# 'secret_route' essa função vai ser executa dentro do 'token_verify'
# primeiro ele vai a verificação lá dentro do token depois ele executa essa função
# posso usar essa função do token em qualquer rota igual lá no c# que ele chama o
# 'CurrentUser' automatico e conseuge pegar mais ou menos isso
def secret_route(token):

    return jsonify({
        'data': 'Mensagem secreta'
    }), 200


@route_bp.route('/auth', methods=["POST"])
def autorization_route():
    token = token_creator.create(uid=12)

    return jsonify({
        'token': token
    }), 200
