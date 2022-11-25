from enum import Enum

from fastapi import APIRouter

from config.database import session
from config.models import GenreDto, Genre

router = APIRouter(
    prefix="/genre",
    tags=["genre"]
)

genre_categories = ["POP", "ROCK", "JAZZ", "ELECTRONIC", "HIPHOP", "R&B", "WORLD", "EXPERIMENTAL"]


def get_category(category: str):
    category = category.upper()

    if category not in genre_categories:
        raise ValueError(f"{category} is not defined.")

    return category


@router.put("")
async def insert_genre(request: GenreDto):
    category = get_category(request.category)
    genre = Genre(category=category, name=request.name)

    session.insert(genre)

    return True
