# Only included the parts you would need to modify

'''
SEE DJANGOPROJECT.COM FOR CONFIGURING SETTINGS.PY AND THE OPTIONS AVAILABLE
'''

# Add the 'properties' app for our properties models - adding 'PropertiesConfig' from properties/apps
INSTALLED_APPS = [
    'properties.apps.PropertiesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# An example of modifying the database setup - we used MySQL for this projects\
# We set options to allow INNODB as the default storage engine - INNODB allows foreign keys
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USERNAME':'username',
        'PASSWORD':'password',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS':{
            'init_command':'SET default_storage_engine=INNODB'
        }
    }
}
