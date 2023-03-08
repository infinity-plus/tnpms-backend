echo Starting Gunicorn.
PORT=${PORT:-8000}
exec gunicorn tnpapp.wsgi --bind 0.0.0.0:$PORT
