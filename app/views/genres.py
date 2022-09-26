from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_services
from app.dao.models.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_services.get_all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        genre_services.create(req_json)

        return "genre add", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        try:
            genre = genre_services.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception:
            return "", 404

    def put(self, gid: int):
        req_json = request.json
        req_json['id'] = gid

        genre_services.update(req_json)

        return "genre put", 204

    def patch(self, gid: int):
        req_json = request.json
        req_json['id'] = gid

        genre_services.update_partial(req_json)

        return "genre patch", 204

    def delete(self, gid: int):
        genre_services.delete(gid)

        return "genre delete", 204
