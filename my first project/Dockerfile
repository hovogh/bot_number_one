FROM python:3.8-slim-buster

RUN pip install pyTelegramBotAPI

WORKDIR /app

COPY . /app

CMD ["python", "test.py"]