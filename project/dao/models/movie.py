from project.dao.models.base import BaseMixin
from project.setup_db import db


class Movie(BaseMixin, db.Model):
    __tablename__ = 'movie'

    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(1000), nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)

    genre = db.relationship("Genre")
    director = db.relationship("Director")

    def __repr__(self):
        return f"<Movie '{self.title.title()}'>"
