import json
from datetime import datetime
from typing import Union

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ARRAY, JSON, DATETIME, func
from .database import Base


class Album(Base):
    __tablename__ = "album"

    album_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250), nullable=False)
    artist_id = Column(Integer, nullable=False)
    image_id = Column(String(32), nullable=False)
    tracks = Column(ARRAY(String), nullable=False)
    release = Column(String, nullable=False)


class AlbumDto(BaseModel):
    album_id: Union[int, None] = None
    title: str
    artist_id: int
    image_id: str
    tracks: list[str]
    release: Union[datetime, None] = None

    def to(self):
        return Album(
            album_id=self.album_id,
            title=self.title,
            artist_id=self.artist_id,
            image_id=self.image_id,
            tracks=json.dumps(self.tracks),
            release=None if self.release is None else self.release.strftime("%Y-%m-%d")
        )


class AlbumGenre(Base):
    __tablename__ = "album_genre"

    album_id = Column(Integer, primary_key=True)
    genre_id = Column(Integer, primary_key=True)


class Genre(Base):
    __tablename__ = "genre"

    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)


class GenreDto(BaseModel):
    genre_id: Union[int, None] = None
    category: str
    name: str

    def to(self):
        return Genre(
            genre_id=self.genre_id,
            category=self.category,
            name=self.name
        )


class Artist(Base):
    __tablename__ = "artist"

    artist_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    name_en = Column(String(100), nullable=True)
    pronounce = Column(String(100), nullable=True)
    nation = Column(String, nullable=False)


class Lecture(Base):
    __tablename__ = "lecture"

    lecture_id = Column(Integer, primary_key=True, autoincrement=True)
    album_id = Column(String, nullable=False)
    rating = Column(Integer, nullable=True)
    date = Column(String(10), nullable=True)
    season_id = Column(String, nullable=False)


class Comment(Base):
    __tablename__ = "comment"

    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_id = Column(Integer, nullable=False)
    writer = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    picks = Column(JSON, nullable=False)
    text = Column(String(500), nullable=False)
    created_at = Column(DATETIME, nullable=False)


class Season(Base):
    __tablename__ = "season"

    season_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image_id = Column(String(50), nullable=False)
