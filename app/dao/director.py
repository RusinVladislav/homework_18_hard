from app.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def create(self, data):
        director = Director(**data)

        self.session.add(Director)
        self.session.commit()

        return director

    def update(self, director):

        self.session.add(Director)
        self.session.commit()

        return director

    def delete(self, did):
        director = self.get_one(did)

        self.session.add(director)
        self.session.commit()
