FROM python:3.9.7-alpine

WORKDIR /app

ADD . /TebUI_Flask

RUN pip install pipenv

WORKDIR /TebUI_Flask

RUN pipenv install --deploy --system

CMD ["python","app.py"]
