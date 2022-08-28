from datetime import datetime
from typing import Optional

from sqlalchemy import (
	DATETIME,
	Integer,
	Unicode,
	Column,
	create_engine,
	ForeignKey,
	Table,
	MetaData,
	Float,
)
from sqlalchemy.orm import registry, relationship

from domain import interface, dataclasses

naming_convention = {
	'ix': 'ix_%(column_0_label)s',
	'uq': 'uq_%(table_name)s_%(column_0_name)s',
	'ck': 'ck_%(table_name)s_%(constraint_name)s',
	'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
	'pk': 'pk_%(table_name)s'
}

# даем имя схемы только для БД MSSQL, связано с инфраструктурными особенностями
metadata = MetaData(naming_convention=naming_convention)

users = Table(
	'users',
	metadata,
	Column('id', Integer, primary_key=True),
	Column('email', Unicode(255), nullable=True),
	Column('fam', Unicode(255), nullable=False),
	Column('name', Unicode(255), nullable=False),
	Column('otc', Unicode(255), nullable=True),
	Column('phone', Unicode(255), nullable=False),
)

coords = Table(
	'coords',
	metadata,
	Column('id', Integer, primary_key=True),
	Column('latitude', Float, nullable=False),
	Column('longitude', Float, nullable=False),
	Column('height', Integer, nullable=False),
)

levels = Table(
	'levels',
	metadata,
	Column('id', Integer, primary_key=True),
	Column('winter', Unicode(255), nullable=False),
	Column('summer', Unicode(255), nullable=False),
	Column('autumn', Unicode(255), nullable=False),
	Column('spring', Unicode(255), nullable=False),
)

images = Table(
	'images',
	metadata,
	Column('id', Integer, primary_key=True),
	Column('data', Unicode(255), nullable=False),
	Column('title', Unicode(255), nullable=False),
)

data = Table(
	'data',
	metadata,
	Column('id', Integer, primary_key=True),
	Column('beauty_title', Unicode(255), nullable=False),
	Column('title', Unicode(255), nullable=False),
	Column('other_titles', Unicode(255), nullable=False),
	Column('connect', Unicode(255), nullable=False),
	Column('add_time', DATETIME, default=datetime.utcnow()),
	Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
	Column('coords_id', Integer, ForeignKey('coords.id'), nullable=False),
	Column('level_id', Integer, ForeignKey('levels.id'), nullable=False),
	Column('images_id', Integer, ForeignKey('images.id'), nullable=False),
)

mapper = registry()

mapper.map_imperatively(dataclasses.User, users)
mapper.map_imperatively(dataclasses.Coords, coords)
mapper.map_imperatively(dataclasses.Level, levels)
mapper.map_imperatively(dataclasses.Image, images)
mapper.map_imperatively(
	dataclasses.Data,
	data,
	properties={
		'user': relationship(
			dataclasses.User,
			backref='data',
			lazy='joined',
		),
		'coords': relationship(
			dataclasses.Coords,
			backref='data',
			lazy='joined',
		),
		'levels': relationship(
			dataclasses.Level,
			backref='data',
			lazy='joined',
		),
		'images': relationship(
			dataclasses.Image,
			backref='data',
			lazy='joined',
		),
	}
)


class Repository(interface.Repository):
	def __init__(self, conn_string: str):
		self.conn_string = conn_string

	def add_data(self, body: dataclasses.Data):
		engine = metadata.cre(self.conn_string, )

