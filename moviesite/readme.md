## How to install requirements.txt file

```
pip install -r requirements.txt
```
## How setup initial database, admin/admin
```
py manage.py makemigrations movies
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver 8089

```