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
        fields = request.args
        return movies_schema.dump(movie_services.get_by_fields(**fields)), 200

        # код из прошлой домашки который выводил постранично movies
        # all_movies = movie_services.get_all()
        # movies = movies_schema.dump(all_movies)
        # director_id = request.args.get('director_id')
        # genre_id = request.args.get('genre_id')
        #
        # # задаем количество элементов на странице
        # LIMIT = 5
        #
        # # получаем значение из адресной строки по ключу "page"
        # page = request.args.get("page")
        #
        # # делаем проверку на полученное значение из адресной страницы
        # if page is None:
        #     page_n = request.args.get("page", 1)
        # elif page.isdigit():
        #     page_n = int(page)
        # else:
        #     page_n = request.args.get("page", 1)
        #
        # # выводим необходимое количество элементов в зависимости от страницы
        # items_to_show = movies[(page_n - 1) * LIMIT:page_n * LIMIT]
        #
        # return items_to_show, 200

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

# Хотел реализовать запросы в отдельные views для movies:
# /movies/?director_id=1
# /movies/?genre_id=1
# /movies/?director_id=2&genre_id=4
# @movie_ns.route('/director/<int:did>')
# class MovieView(Resource):
#     def get(self, did: int):
#         try:
#             director = director_services.get_one(did)
#             return movies_schema.dump(director), 200
#         except Exception:
#             return "", 404
#
#
# @movie_ns.route('/genre/<int:gid>')
# class MovieView(Resource):
#     def get(self, gid: int):
#         try:
#             genre = genre_services.get_one(gid)
#             return movies_schema.dump(genre), 200
#         except Exception:
#             return "", 404
#
#
# @movie_ns.route('/director/<int:did>/genre/<int:gid>')
# class MovieView(Resource):
#     def get(self, did: int, gid: int):
#         try:
#             movie = db.session.query(Movie).filter(Movie.director_id == did, Movie.genre_id == gid).all()
#             return movies_schema.dump(movie), 200
#         except Exception:
#             return "", 404
