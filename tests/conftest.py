from datetime import datetime, date

import pytest
from domain import dataclasses


@pytest.fixture(scope='function')
def user():
    return dataclasses.User(
        id=1,
        phone="+7 555 55 55",
        fam="Пупкин",
        name="Василий",
        email='qwerty@mail.ru',
        otc='Иванович'
    )


@pytest.fixture(scope='function')
def coords():
    return dataclasses.Coords(
        id=1,
        latitude=45.3842,
        longitude=7.1525,
        height=1200
    )


@pytest.fixture(scope='function')
def level():
    return dataclasses.Level(
        id=1,
        winter='2B',
        summer='1А',
        autumn='1А',
        spring='2B'
    )


@pytest.fixture(scope='function')
def img():
    return dataclasses.Image(
        id=1,
        img='\\x8534234568...',
        title='Седловина',
        pereval_id=1,
        date_added=date.today()
    )


@pytest.fixture(scope='function')
def pereval():
    return dataclasses.PerevalAdded(
        id=1,
        date_added=date.today(),
        beauty_title='пер. ',
        title='Пхия',
        other_titles='Триев',
        connect='Текстовое поле',
        add_time=datetime.utcnow(),
        user_id=1,
        coords_id=1,
        level_id=1,
        status=False
    )


@pytest.fixture(scope='function')
def pereval_info_response():
    return dataclasses.PerevalInfoResponse(
        id=1,
        beauty_title='пер. ',
        title='Пхия',
        other_titles='Триев',
        connect='Текстовое поле',
        add_time=datetime.utcnow(),
        coords={
            'latitude': 45.3842,
            'longitude': 7.1525,
            'height': 1200
        },
        level={
            'winter': '2B',
            'summer': '1А',
            'autumn': '1А',
            'spring': '2B',
        },
        images=[
            {
                'img': '\\x8534234568...',
                'title': 'Седловина'
            }
        ],
        status=False
    )


@pytest.fixture(scope='function')
def pereval_info():
    return dataclasses.PerevalInfo(
        id=1,
        beauty_title='пер. ',
        title='Пхия',
        other_titles='Триев',
        connect='Текстовое поле',
        add_time=datetime.utcnow(),
        user={
            'email': 'qwerty@mail.ru',
            'fam': 'Пупкин',
            'name': 'Василий',
            'otc': 'Иванович',
            'phone': '+7 555 55 55'
        },
        coords={
            'latitude': 45.3842,
            'longitude': 7.1525,
            'height': 1200
        },
        level={
            'winter': '2B',
            'summer': '1А',
            'autumn': '1А',
            'spring': '2B',
        },
        images=[
            {
                'img': '\\x8534234568...',
                'title': 'Седловина'
            }
        ],
        status=False
    )
