# django-apps
This Repo contains django apps created as part of HTI python django course


#####Start project 
django-admin startproject finance_project

#####start app 
cd finance_project 

##### add app name to installed apps in settings.py

##### database settings 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finance_project',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

##### First db migrate
python manage.py migrate

##### make Models entries 



##### runserver 
python manage.py runserver

##### superuser-password
Admin@123

##### Static
STATICFILES_DIRS is need to be set carefully for your local static files when running in debug = True mode 



