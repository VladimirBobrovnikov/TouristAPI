from fastapi import FastAPI


from domain.service import MobileTourist
from domain.dataclasses import Body


app = FastAPI()


class Controller:
	def __init__(self, service: MobileTourist):
		self.service = service

	@app.post('/submitData')
	def submit_data(self, body: Body):
		self.service.add_data(body=body)
		return {'added': 'success'}
