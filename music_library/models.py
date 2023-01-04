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
    date: datetime = None
    description: str = None
    youtube_link: str = None
    spotify_link: str = None
    
