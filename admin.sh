docker exec -it backend bash
cd level-up-academy/level_up_academy
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser