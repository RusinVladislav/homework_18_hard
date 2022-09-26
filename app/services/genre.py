from app.dao.genre import GenreDAO


class GenreServices:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, did):
        return self.dao.get_one(did)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        did = data.get("id")
        genre = self.get_one(did)

        genre.name = data.get('name')

        self.dao.update(genre)

    def update_partial(self, data):
        did = data.get("id")
        genre = self.get_one(did)

        if "name" in data:
            genre.name = data.get('name')

        self.dao.update(genre)

    def delete(self, did):
        self.dao.delete(did)
