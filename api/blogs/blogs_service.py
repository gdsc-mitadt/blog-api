import json

from flask import Response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, ValidationError, DoesNotExist

from api.basic_errors import InternalServerError, SchemaValidationError, NoAuthorizationError
from api.blogs.blogs_model import *

class BasicBlogsApi(Resource):
    # @jwt_required()
    def get(self):
        try:
            return jsonify(Blogs.objects())
        except NoAuthorizationError:
            raise NoAuthorizationError

    # @jwt_required()
    def post(self):
        try:
            body = request.get_json()
            datetime_now = datetime.utcnow()
            body['created_on'] = datetime_now
            body['modified_on'] = datetime_now
            blog = Blogs(**body).save()
            blog.save()
            id = blog.id
            return {'id': str(id)}, const.status_created_201
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError

class BlogsByIdApi(Resource):
    def get(self,id):
        try:
            return jsonify(Blogs.objects.get(id=id))
        except NoAuthorizationError:
            raise NoAuthorizationError
    def delete(self,id):
        try:
            Blogs.objects.get(id=id).delete()
            return {"message":"Deleted successfully"}, const.status_ok_200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError