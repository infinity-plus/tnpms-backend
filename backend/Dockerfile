FROM python:3.10.8-alpine3.16

RUN mkdir /workdir
WORKDIR /workdir

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /workdir/
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT [ "gunicorn","djangorest.wsgi", "--bind", "0.0.0.0:8000" ]