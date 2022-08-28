FROM python:3.7
WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "run:app.app", "--host", "0.0.0.0", "--port", "1234"]

