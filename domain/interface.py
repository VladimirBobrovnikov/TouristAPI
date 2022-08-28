from abc import ABC, abstractmethod

from domain.dataclasses import Body


class Repository(ABC):

	@abstractmethod
	def add_data(self, body: Body):
		...
