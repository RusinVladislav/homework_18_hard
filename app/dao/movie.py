from app.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()
        
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        
        self.session.add(movie)
        self.session.commit()

    def get_by_fields(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()
