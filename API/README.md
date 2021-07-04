# API flask app

## Run
export APP_SETTINGS="config.Config"
export DATABASE_URL="sqlite:///database.sqlite3"
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver