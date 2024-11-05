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



# in your project folder update file called settings.py 

1.update under INSTALLED_APPS section

```bash
'rest_framework',
    'api'
```
2.update DATABASES = section
```bash
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',     # Replace with your database name
        'USER': 'postgres',           # Replace with your PostgreSQL username
        'PASSWORD': '.*******',       # Replace with your PostgreSQL password
        'HOST': 'localhost',               # Typically 'localhost' or '127.0.0.1'
        'PORT': '5432',                    # Default PostgreSQL port
    }
```


# in your api folder 

1.code models.py

2.in code editor terminal migrate process
```bash
python manage.py makemigrations
python manage.py migrate
````

3.add/create file called under api serializer.py
    code 

4.code file callled views.py under api

5.add/create file called under api urls.py
    code 


# in your project folder

1.update/edit file called urls.py

# Run
```bash
python manage.py runserver
```
