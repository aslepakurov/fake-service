FROM python:3.9-alpine

ADD . /src
WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app"]