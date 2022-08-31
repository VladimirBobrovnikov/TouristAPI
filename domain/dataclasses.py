from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, Field
from dataclasses import dataclass


class UserInfo(BaseModel):
    email: Optional[str] = Field(default=None, description='Эл. почта пользователя', example='qwerty@mail.ru')
    fam: str = Field(description='Фамилия пользователя', example='Пупкин')
    name: str = Field(description='Имя пользователя', example='Василий')
    otc: Optional[str] = Field(default=None, description='Отчество пользователя', example='Иванович')
    phone: str = Field(description='Телефон пользователя', example='+7 555 55 55')


class CoordsInfo(BaseModel):
    latitude: float = Field(description='Широта', example=45.3842)
    longitude: float = Field(description='пользователя', example=7.1525)
    height: int = Field(description='пользователя', example=1200)


class LevelInfo(BaseModel):
    winter: str = Field(description='Категория трудности. Зима.', example='')
    summer: str = Field(description='Категория трудности. Лето.', example='1А')
    autumn: str = Field(description='Категория трудности. Осень', example='1А')
    spring: str = Field(description='Категория трудности. Весна.', example='')


class ImageInfo(BaseModel):
    img: str = Field(description='Фото в Bytes', example='\\x8534234568...')
    title: str = Field(description='Название фото', example='Седловина')


class BodyInfo(BaseModel):
    beauty_title: str = Field(description='Сокращенное название', example='пер. ')
    title: str = Field(description='Название', example='Пхия')
    other_titles: str = Field(description='Народное название', example='Триев')
    connect: str = Field(description='Что соединяет', example='Текстовое поле')
    add_time: datetime = Field(description='Время добавления', example=datetime.utcnow().isoformat())
    user: UserInfo = Field(
        description='Пользователь',
        example={
            'email': 'qwerty@mail.ru',
            'fam': 'Пупкин',
            'name': 'Василий',
            'otc': 'Иванович',
            'phone': '+7 555 55 55'
        }
    )
    coords: CoordsInfo = Field(
        description='Координаты перевала',
        example={
            'latitude': 45.3842,
            'longitude': 7.1525,
            'height': 1200
        }
    )
    level: LevelInfo = Field(
        description='Уровень сложности',
        example={
            'winter': '2B',
            'summer': '1А',
            'autumn': '1А',
            'spring': '2B',
        }
    )
    images: List[ImageInfo] = Field(
        description='Картинки',
        example=[
            {
                'img': '\\x8534234568...',
                'title': 'Седловина'
            }
        ]
    )


class PerevalInfo(BodyInfo):
    status: bool = Field(description='Статус прохождения модерации', example=False)


@dataclass
class User:
    phone: str
    fam: str
    name: str
    id: Optional[int] = None
    email: Optional[str] = None
    otc: Optional[str] = None


@dataclass
class Coords:
    latitude: float
    longitude: float
    height: int
    id: Optional[int] = None


@dataclass
class Level:
    winter: str
    summer: str
    autumn: str
    spring: str
    id: Optional[int] = None


@dataclass
class Image:
    img: str
    title: str
    pereval_id: int
    date_added: date
    id: Optional[int] = None


@dataclass
class PerevalAdded:
    date_added: Optional[date]
    beauty_title: str
    title: str
    other_titles: str
    connect: str
    add_time: datetime
    user_id: int
    coords_id: int
    level_id: int
    id: Optional[int] = None
    status: Optional[bool] = False
