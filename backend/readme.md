# Django Rest Framework API

## Running the project in production

### 1. Cloning the project
```
git clone https://github.com/jeelpatel231/django-rest-api-proto
```
> its implicit that you will cd into the dir


### 2. Installing pre-requisites
```
pip3 install -r requirements.txt
```

### 3. Configuring your environment
```
edit the "sample.env" file according to your needs, and rename is to ".env"
```
> mv sample.env .env

### 4. Making Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Collecting Static Files *
```
python manage.py collectstatic
```
##### * = skippable step if in development environment

### 6. Running the server
```
python manage.py runserver
```
_______

### Creating new migrations
Make your preferred models in user/models.py
with respected serializers in users/serializers.py
and apiviews in models/views.py.

Run the following command to generate migrations
```
python manage.py makemigrations
python manage.py migrate
```

_______

## Building the docker image

**You will need to have .env file in the project directory to build the docker image**
While building docker image, collectstatic uses settings.py > SECRET_KEY variable, which will be defined with environment variable.
Use the sample.env file for instructions.

```
docker build -t placement-api-proto .
```

### Running the docker image
```
docker run -p 8000:8000 placement-api-proto
```
