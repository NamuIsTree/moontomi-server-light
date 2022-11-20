from sqlalchemy import Column, Integer, String, ARRAY
from .database import Base


class Album(Base):
    __tablename__ = "album"

    album_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250), nullable=False)
    artist_id = Column(Integer, nullable=False)
    image_id = Column(Integer, nullable=False)
    genres = Column(ARRAY(Integer), nullable=False)
    tracks = Column(ARRAY(String), nullable=False)
    release = Column(String, nullable=False)


class Genre(Base):
    __tablename__ = "genre"

    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    name = Column(String, nullable=True)


class Artist(Base):
    __tablename__ = "artist"

    artist_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    nation = Column(String, nullable=False)


class Lecture(Base):
    __tablename__ = "lecture"

    lecture_id = Column(Integer, primary_key=True, autoincrement=True)
    ymd = Column(String, nullable=True)
    album_id = Column(String, nullable=False)
    season = Column(String, nullable=False)
