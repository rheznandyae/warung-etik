migrate: python manage.py migrate
web: daphne warung_etik.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=warung_etik.settings -v2