from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_services
from app.dao.models.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_services.get_all()
        movies = movies_schema.dump(all_movies)

        # задаем количество элементов на странице
        LIMIT = 5

        # получаем значение из адресной строки по ключу "page"
        item = request.args.get("page")

        # делаем проверку на полученное значение из адресной страницы
        if item is None:
            page_n = request.args.get("page", 1)
        elif item.isdigit():
            page_n = int(item)
        else:
            page_n = request.args.get("page", 1)

        # выводим необходимое количество элементов в зависимости от страницы
        items_to_show = movies[(page_n - 1) * LIMIT:page_n * LIMIT]

        return items_to_show, 200

    def post(self):
        req_json = request.json
        movie_services.create(req_json)

        return "Movie add", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        try:
            movie = movie_services.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception:
            return "", 404

    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_services.update(req_json)

        return "Move put", 204

    def patch(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_services.update_partial(req_json)

        return "Move patch", 204

    def delete(self, mid: int):
        movie_services.delete(mid)
        
        return "Move delete", 204


# @movie.route('/director/<int:did>')
# class MovieView(Resource):
#     def get(self, did: int):
#         try:
#             movie = db.session.query(Movie).filter(Movie.director_id == did).all()
#             return movies_schema.dump(movie), 200
#         except Exception:
#             return "", 404
#
#
# @movie.route('/genre/<int:gid>')
# class MovieView(Resource):
#     def get(self, gid: int):
#         try:
#             movie = db.session.query(Movie).filter(Movie.genre_id == gid).all()
#             return movies_schema.dump(movie), 200
#         except Exception:
#             return "", 404
#
#
# @movie.route('/director/<int:did>/genre/<int:gid>')
# class MovieView(Resource):
#     def get(self, did: int, gid: int):
#         try:
#             movie = db.session.query(Movie).filter(Movie.director_id == did, Movie.genre_id == gid).all()
#             return movies_schema.dump(movie), 200
#         except Exception:
#             return "", 404
