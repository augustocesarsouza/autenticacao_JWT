from functools import wraps
import jwt
from flask import jsonify, request
from .token_handler import  token_creator
from src.config.jwt_config_file import jwt_config


def token_verify(function: callable) -> callable:
    
    @wraps(function)
    def decorated(*agr, **kwargs):
        raw_token = request.headers.get("Authorization")
        uid = request.headers.get('uid')

        if not raw_token or not uid:
            return jsonify({
                'error': "Nao Autorizado"
            }), 400

        if not raw_token:
            return jsonify({
                'error': "Nao Autorizado"
            }), 401

        try:
            token = raw_token.split()[1]
            print(token)
            token_information = jwt.decode(token, key=jwt_config["JWT_KEY"], algorithms="HS256")
            token_uid = token_information["uid"]
        except jwt.InvalidSignatureError:
            return jsonify({
                'error': "Token Invalido"
            }), 401 
        except jwt.ExpiredSignatureError:
            return jsonify({
                'error': "Token Expirado"
            }), 401 
        except KeyError as e:
            return jsonify({
                'error': "Token Invalido2"
            }), 401 
        
        if int(token_uid) != int(uid):
            return jsonify({
                'error': "user nao permitido"
            }), 400
        
        next_token = token_creator.refresh(token)
        
        return function(next_token, *agr, **kwargs)
    
    return decorated