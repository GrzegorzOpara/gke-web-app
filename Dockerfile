FROM python:3.11-alpine

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV PORT=8080
EXPOSE 8080

CMD [ "python3", "app.py"]