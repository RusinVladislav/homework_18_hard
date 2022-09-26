from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.database import db
from app.services.director import DirectorServices
from app.services.genre import GenreServices
from app.services.movie import MovieServices

movie_dao = MovieDAO(db.session)
movie_services = MovieServices(movie_dao)

director_dao = DirectorDAO(db.session)
director_services = DirectorServices(director_dao)

genre_dao = GenreDAO(db.session)
genre_services = GenreServices(genre_dao)
