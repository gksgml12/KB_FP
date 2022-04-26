
#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'test', #2
        'USER': 'root', #3
        'PASSWORD': 'password',  #4
        'HOST': 'localhost',   #5
        'PORT': '3306', #6
    }
}
SECRET_KEY = 'django-insecure-9ckas-r^g1g3%xinzs0#k$ixe3ih%5#0l%u#407+7ua6)2)m+q'
