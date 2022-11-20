import ast

from fastapi import APIRouter, Response
from sqlalchemy import or_
from sqlalchemy.exc import NoResultFound

from config.database import session
from config.models import Album, Artist, Lecture, Genre

router = APIRouter(
    prefix="/lecture",
    tags=["lecture"]
)


@router.get("/search")
async def search_lectures(page: int, page_size: int, sort_by: str, sort_option: str, search: str = ""):
    if sort_by not in ['rating', 'id']:
        return Response(status_code=400)

    page = max(page, 1)
    page_size = min(max(page_size, 1), 15)

    query = session.query(
        Lecture.lecture_id, Album.title, Album.image_id, Artist.name, Artist.nation
    ).filter(
        Lecture.album_id == Album.album_id
    ).filter(
        Album.artist_id == Artist.artist_id
    )

    if sort_by == 'id':
        if sort_option == 'asc':
            query = query.order_by(Lecture.lecture_id.asc())
        else:
            query = query.order_by(Lecture.lecture_id.desc())

    if not len(search) == 0:
        query = query.filter(
            or_(
                Album.title.contains(search),
                Artist.name.contains(search),
                Artist.nation.contains(search)
            )
        )

    result = query.limit(page_size).offset((page - 1) * page_size).all()
    return result


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
