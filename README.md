Steve Baker Beepscore LLC

# Purpose
Record info about django tutorial.

# References

Writing your first Django app, part 1
https://docs.djangoproject.com/en/1.7/intro/tutorial01/

http://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv

# Results

## virtualenv and virtualenvwrapper
Use pre-installed Python 3.
install Django 1.7
virtualenv -p /usr/local/bin/python3 mysite
or
mkvirtualenv -p /usr/local/bin/python3 mysite

    ➜  pythonProjects  mkvirtualenv -p /usr/local/bin/python3 mysite
    Running virtualenv with interpreter /usr/local/bin/python3
    Using base prefix '/usr/local/Cellar/python3/3.4.2_1/Frameworks/Python.framework/Versions/3.4'
    New python executable in mysite/bin/python3.4
    Also creating executable in mysite/bin/python
    Installing setuptools, pip...done.

    lsvirtualenv

    (mysite)➜  pythonProjects  pip install django
    Successfully installed django-1.7.1

    (mysite)➜  pythonProjects  python --version
    Python 3.4.2

    (mysite)➜  pythonProjects  python -c "import django; print(django.get_version())"
    1.7.1

## Create project
    (mysite)➜  pythonProjects  django-admin.py startproject mysite

## Create database
"The migrate command looks at the INSTALLED_APPS setting and
creates any necessary database tables according to
the database settings in your mysite/settings.py file and
the database migrations shipped with the app."

    (mysite)➜  mysite git:(master) python manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying sessions.0001_initial... OK

