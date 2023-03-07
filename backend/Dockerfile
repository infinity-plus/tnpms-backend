FROM python:3.10.8-slim-buster

RUN mkdir /workdir
WORKDIR /workdir

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /workdir

RUN cp sample.env .env
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput
RUN DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_EMAIL=admin@admin.com python manage.py createsuperuser --noinput

EXPOSE 8000

ENTRYPOINT [ "gunicorn","tnpapp.wsgi", "--bind", "0.0.0.0:8000" ]
