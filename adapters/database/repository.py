from datetime import datetime, date
from typing import Optional, Dict, List, Any, Union

from sqlalchemy import (
	insert,
	select,
	update,
	delete,
)

from domain import interface, dataclasses


class UserRepo(interface.UserRepo):
	def __init__(self, engine):
		self.engine = engine

	def add_user(self, user: Dict) -> int:
		query = insert(dataclasses.User, user)
		result = self.engine.execute(query)
		return result.inserted_primary_key[0]

	def get_user_by_phone(self, user_phone: str) -> Optional[dataclasses.User]:
		query = select(dataclasses.User).where(dataclasses.User.phone == user_phone)
		row = self.engine.execute(query).one_or_none()
		return dataclasses.User(**row) if row is not None else None

	def get_user_by_id(self, user_id: int) -> Optional[dataclasses.User]:
		query = select(dataclasses.User).where(dataclasses.User.id == user_id)
		row = self.engine.execute(query).one_or_none()
		return dataclasses.User(**row) if row is not None else None


class ImgRepo(interface.ImgRepo):
	def __init__(self, engine):
		self.engine = engine

	def add_image(self, image: Dict) -> int:
		query = insert(dataclasses.Image, image)
		result = self.engine.execute(query)
		return result.inserted_primary_key[0]

	def get_imgs_by_pereval_id(self, pereval_id: int) -> List[dataclasses.Image]:
		query = select(dataclasses.Image).where(dataclasses.Image.pereval_id == pereval_id)
		rows = self.engine.execute(query).all()
		return [dataclasses.Image(**row) for row in rows]

	def edit_imgs(self, pereval_id: int, images: List[Dict[str, Any]]) -> None:
		old_img_ids = self.engine.execute(
			select(dataclasses.Image.id).where(dataclasses.Image.pereval_id == pereval_id)
		).scalars().all()

		len_list_old_img = len(old_img_ids)

		for index_new_img in range(len(images)):
			if index_new_img < len_list_old_img:
				query = update(
					dataclasses.Image
				).where(
					dataclasses.Image.id == old_img_ids[index_new_img]
				).values(
					img=images[index_new_img]['img'],
					title=images[index_new_img]['title'],
					date_added=date.today()
				)
			else:
				query = insert(
					dataclasses.Image
				).values(
					img=images[index_new_img]['img'],
					title=images[index_new_img]['title'],
					pereval_id=pereval_id,
					date_added=date.today()
				)
			self.engine.execute(query)

		if not len(images):
			index_new_img = 0

		if len_list_old_img < index_new_img:
			for index in range(index_new_img, len_list_old_img):
				query = delete(
					dataclasses.Image
				).where(
					dataclasses.Image.id == old_img_ids[index]
				)
				self.engine.execute(query)


class PerevalRepository(interface.PerevalRepository):
	def __init__(self, engine):
		self.engine = engine

	def add_data(self, data_for_add: Dict) -> int:
		query = insert(dataclasses.PerevalAdded, data_for_add)
		result = self.engine.execute(query)
		return result.inserted_primary_key[0]

	def add_coords(self, coords: Dict) -> int:
		query = insert(dataclasses.Coords, coords)
		result = self.engine.execute(query)
		return result.inserted_primary_key[0]

	def add_level(self, level: Dict) -> int:
		query = insert(dataclasses.Level, level)
		result = self.engine.execute(query)
		return result.inserted_primary_key[0]

	def get_pereval(self, pereval_id: int) -> Optional[dataclasses.PerevalAdded]:
		query = select(dataclasses.PerevalAdded).where(dataclasses.PerevalAdded.id == pereval_id)
		row = self.engine.execute(query).one_or_none()
		return dataclasses.PerevalAdded(**row) if row is not None else None

	def get_coords_by_id(self, coords_id: int) -> Optional[dataclasses.Coords]:
		query = select(dataclasses.Coords).where(dataclasses.Coords.id == coords_id)
		row = self.engine.execute(query).one_or_none()
		return dataclasses.Coords(**row) if row is not None else None

	def get_levels_by_id(self, level_id: int) -> Optional[dataclasses.Level]:
		query = select(dataclasses.Level).where(dataclasses.Level.id == level_id)
		row = self.engine.execute(query).one_or_none()
		return dataclasses.Level(**row) if row is not None else None

	def edit_pereval(self, pereval_id: int, pereval: Dict[str, str]) -> None:
		query = update(
			dataclasses.PerevalAdded
		).where(
			dataclasses.PerevalAdded.id == pereval_id
		).values(**pereval)
		self.engine.execute(query)

	def edit_coords(self, coords_id: int, coords: Dict[str, Union[float, int]]) -> None:
		query = update(
			dataclasses.Coords
		).where(
			dataclasses.Coords.id == coords_id
		).values(**coords)
		self.engine.execute(query)

	def edit_levels(self, levels_id: int, levels: Dict[str, str]) -> None:
		query = update(
			dataclasses.Level
		).where(
			dataclasses.Level.id == levels_id
		).values(**levels)
		self.engine.execute(query)

	def get_data_by_email(self, user_email: str) -> List[dataclasses.PerevalInfoResponse]:
		query = select(
			dataclasses.PerevalAdded.id,
			dataclasses.PerevalAdded.date_added,
			dataclasses.PerevalAdded.beauty_title,
			dataclasses.PerevalAdded.title,
			dataclasses.PerevalAdded.other_titles,
			dataclasses.PerevalAdded.connect,
			dataclasses.PerevalAdded.add_time,
			dataclasses.PerevalAdded.status,
			dataclasses.Image.title,
			dataclasses.Image.img,
			dataclasses.Level.winter,
			dataclasses.Level.summer,
			dataclasses.Level.autumn,
			dataclasses.Level.spring,
			dataclasses.Coords.latitude,
			dataclasses.Coords.longitude,
			dataclasses.Coords.height
		).join(
			dataclasses.User, dataclasses.PerevalAdded.user_id == dataclasses.User.id
		).join(
			dataclasses.Image, dataclasses.PerevalAdded.id == dataclasses.Image.pereval_id
		).join(
			dataclasses.Level, dataclasses.PerevalAdded.level_id == dataclasses.Level.id
		).join(
			dataclasses.Coords, dataclasses.PerevalAdded.coords_id == dataclasses.Coords.id
		).where(dataclasses.User.email == user_email)
		rows = self.engine.execute(query).all()
		result = list()
		for row in rows:
			obj = self._create_objects(*row)
			if len(result) and obj.id == result[-1].id:
				result[-1].images.extend(obj.images)
			else:
				result.append(obj)
		return result

	def _create_objects(
			self,
			pereval_id: int,
			date_added: date,
			beauty_title: str,
			pereval_title: str,
			other_titles: str,
			connect: str,
			add_time: datetime,
			status: bool,
			img_title: str,
			img: str,
			winter: str,
			summer: str,
			autumn: str,
			spring: str,
			latitude: float,
			longitude: float,
			height: int
	) -> dataclasses.PerevalInfoResponse:

		coords = {
			'latitude': latitude,
			'longitude': longitude,
			'height': height
		}
		level = {
			'winter': winter,
			'summer': summer,
			'autumn': autumn,
			'spring': spring
		}
		image = [
			{
				'title': img_title,
				'img': img,
			}
		]

		return dataclasses.PerevalInfoResponse(
			id=pereval_id,
			date_added=date_added,
			beauty_title=beauty_title,
			title=pereval_title,
			other_titles=other_titles,
			connect=connect,
			add_time=add_time,
			coords=coords,
			level=level,
			images=image,
			status=status
		)

