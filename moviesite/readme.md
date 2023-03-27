## How to install requirements.txt file

```
pip install -r requirements.txt
```
## How setup initial database, admin/admin
```
py manage.py makemigrations movies
py manage.py migratesource
py manage.py createsuperuser
py manage.py runserver 8089

```
## How to create an environment
```
py -m venv .movies
```