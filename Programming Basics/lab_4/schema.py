from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

film_actor_association = Table(
    "film_actor_association",
    Base.metadata,
    Column("film_id", Integer, ForeignKey("films.id")),
    Column("actor_id", Integer, ForeignKey("actors.id"))
)

class Film(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    director_id = Column(Integer, ForeignKey("directors.id"))
    director = relationship("Director", back_populates="films")
    actors = relationship(
        "Actor",
        secondary=film_actor_association,
        back_populates="films"
    )

class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    films = relationship("Film", back_populates="director")

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    films = relationship(
        "Film",
        secondary=film_actor_association,
        back_populates="actors"
    )
