from flask import request
from flask_restx import Resource, Namespace

from app.container import director_services
from app.dao.models.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_services.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_services.create(req_json)
        
        return "Director add", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        try:
            director = director_services.get_one(did)
            return director_schema.dump(director), 200
        except Exception:
            return "", 404

    def put(self, did: int):
        req_json = request.json
        req_json['id'] = did

        director_services.update(req_json)
        
        return "Director put", 204

    def patch(self, did: int):
        req_json = request.json
        req_json['id'] = did

        director_services.update_partial(req_json)
        
        return "Director patch", 204

    def delete(self, did: int):
        director_services.delete(did)
        
        return "Director delete", 204
