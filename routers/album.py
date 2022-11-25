import ast
import traceback

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound

from config.database import session
from config.models import Album, Genre, Artist, AlbumDto, GenreDto, AlbumGenre

router = APIRouter(
    prefix="/album",
    tags=["album"]
)


class AlbumCreationRequest(BaseModel):
    album: AlbumDto
    genres: list[GenreDto]


@router.get("/{album_id}")
async def get_album(album_id: int):
    result = dict(
        session.query(
            Album.title, Album.image_id, Album.tracks, Album.release
        ).filter(
            Album.album_id == album_id
        ).one()
    )

    genres = dict(
        session.query(
            Genre.category, Genre.name
        ).filter(
            and_(
                AlbumGenre.album_id == album_id,
                AlbumGenre.genre_id == Genre.genre_id
            )
        ).all()
    )

    result['genres'] = genres
    result['tracks'] = ast.literal_eval(result['tracks'])

    return result


@router.post("/{album_id}")
async def update_album():
    return


@router.put("")
async def insert_album(request: AlbumCreationRequest):
    album = request.album.to()
    genres = list(get_genre_id(genre.to()) for genre in request.genres)

    session.insert(album)
    session.refresh(album)

    album_genres = []
    for genre_id in genres:
        album_genre = AlbumGenre(album_id=album.album_id, genre_id=genre_id)
        album_genres.append(album_genre)

    session.insert_all(album_genres)

    return {
        "success": True,
        "album_id": album.album_id
    }


def get_genre_id(genre: Genre):
    genre_id = -1

    try:
        result = session.query(
            Genre.genre_id
        ).filter(
            and_(
                Genre.category == genre.category,
                Genre.name == genre.name
            )
        ).one()

        return int(result.genre_id)

    except NoResultFound:
        session.insert(genre)
        session.refresh(genre)
        return int(genre.genre_id)
