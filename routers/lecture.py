import ast

from fastapi import APIRouter, Response
from sqlalchemy.exc import NoResultFound

from config.database import session
from config.models import Album, Artist, Lecture, Genre

router = APIRouter(
    prefix="/lecture",
    tags=["lecture"]
)


@router.get("/{lecture_id}")
async def get_lecture(lecture_id: int):

    try:
        result = session.query(
            Lecture, Album, Artist
        ).filter(
            Lecture.lecture_id == lecture_id
        ).filter(
            Lecture.album_id == Album.album_id
        ).filter(
            Album.artist_id == Artist.artist_id
        ).one()

        lecture = result["Lecture"]
        album = result["Album"]
        artist = result["Artist"]
    except NoResultFound:
        return Response(status_code=204)

    album_genres = ast.literal_eval(album.genres)
    genres = session.query(Genre).filter(Genre.genre_id.in_(album_genres)).all()

    return {
        "id": lecture.lecture_id,
        "date": lecture.ymd,
        "album": {
            "id": album.album_id,
            "title": album.title,
            "artist": {
                "id": artist.artist_id,
                "name": artist.name
            },
            "genres": genres,
            "tracks": ast.literal_eval(album.tracks),
            "release": album.release
        },
        "season": lecture.season
    }
