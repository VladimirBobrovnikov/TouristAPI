import logging

from domain.interface import Repository
from domain.dataclasses import Body


class MobileTourist:
	def __init__(self, repository: Repository, logger: logging.Logger):
		self.repo = repository
		self.logger = logger

	def add_data(self, body: Body):
		return self.repo.add_data(body=body)

