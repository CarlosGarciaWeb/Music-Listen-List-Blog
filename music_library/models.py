from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Song:
    _id: str
    name: str
    author: str
    genre: str
    album: str
    rating: int = 0
    year: int = 0
    members: list[str] = field(default_factory=list)
    date: datetime = None
    description: str = None
    youtube_link: str = None
    spotify_link: str = None
    
