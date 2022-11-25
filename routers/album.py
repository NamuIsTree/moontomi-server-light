import ast

from fastapi import APIRouter
from sqlalchemy import and_

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
            and_(
                Album.artist_id == Artist.artist_id,
                Album.album_id == album_id
            )
        ).one()
    )

    # set genre
    genres = ast.literal_eval(result["genres"])
    result["genres"] = session.query(
        Genre.category, Genre.name
    ).filter(
        Genre.genre_id.in_(genres)
    ).all()

    # set tracks
    result["tracks"] = ast.literal_eval(result["tracks"])

    return result


@router.post("/{album_id}")
async def update_album():
    return


@router.put("")
async def insert_album():
    return
