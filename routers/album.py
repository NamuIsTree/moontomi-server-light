import ast

from fastapi import APIRouter
from config.database import session
from config.models import Album, Genre, Artist

router = APIRouter(
    prefix="/album",
    tags=["album"]
)


@router.get("/all")
async def get_albums_all():
    albums = session.query(Album).all()
    return albums


@router.get("/{album_id}")
async def get_album(album_id: int):
    result = session.query(
        Album, Artist
    ).filter(
        Album.artist_id == Artist.artist_id
    ).filter(
        Album.album_id == album_id
    ).one()

    album = result["Album"]
    artist = result["Artist"]

    album_genres = ast.literal_eval(album.genres)
    genres = session.query(Genre).filter(Genre.genre_id.in_(album_genres)).all()

    return {
        "album_id": album_id,
        "title": album.title,
        "artist": artist,
        "image_id": album.image_id,
        "genres": genres,
        "tracks": ast.literal_eval(album.tracks),
        "release": album.release
    }


@router.post("/{album_id}")
async def update_album():
    return


@router.put("")
async def insert_album():
    return
