FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -U pip && pip install pipenv
RUN pipenv install --deploy --system --ignore-pipfile
