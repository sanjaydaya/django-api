# POST,GET Function Django API
## PostgreSQL Data-Base
## create new folder on code editor for new project



open terinal on code editor(in my case VScode), check python version
```bash
python --version
```
install django
```bash
pip install django djangorestframework
```
install postgre
```bash
pip install  psycopg2
```


create project folder
```bash
django-admin startproject  <your project name>
```
change directory to you project
```bash
cd <your_project/>
```

create api folder
```bash
python manage.py startapp api
```

in your project folder update file called settings.py
```bash
pip install requests
```
add file called views.py on your project (Write request function in views.py, with api
from which you want Data.)

edit file called urls.py (Set URL for that view function)

add file home.html (Display from template)

run project
```bash
python manage.py runserver
```
