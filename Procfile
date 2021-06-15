release: python manage.py makemigrations --no-
release: python manage.py migrate --no-

web: gunicorn AuthLogin.wsgi
