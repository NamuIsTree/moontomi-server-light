import ast

from fastapi import APIRouter
from config.database import session
from config.models import Album, Genre, Artist

router = APIRouter(
    prefix="/album",
    tags=["album"]
)


@router.get("/{album_id}")
async def get_album(album_id: int):
    result = dict(
        session.query(
            Album.album_id, Album.title, Artist.artist_id, Album.image_id, Album.genres, Album.tracks, Album.release
        ).filter(
            Album.artist_id == Artist.artist_id
        ).filter(
            Album.album_id == album_id
        ).one()
    )

    genres = ast.literal_eval(result["genres"])
    genres = session.query(
        Genre.category, Genre.name
    ).filter(
        Genre.genre_id.in_(genres)
    ).all()

    tracks = ast.literal_eval(result["tracks"])

    result["genres"] = genres
    result["tracks"] = tracks

    return result


@router.post("/{album_id}")
async def update_album():
    return


@router.put("")
async def insert_album():
    return
