migrate: python3 manage.py migrate
web: daphne warung_etik.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=warung_etik.settings -v2