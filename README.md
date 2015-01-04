Steve Baker Beepscore LLC

# Purpose
Record info about django tutorial.

# References

Writing your first Django app, part 1  
https://docs.djangoproject.com/en/1.7/intro/tutorial01/
https://docs.djangoproject.com/en/1.7/intro/tutorial02/
https://docs.djangoproject.com/en/1.7/intro/tutorial03/
https://docs.djangoproject.com/en/1.7/intro/tutorial04/

http://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv

# Results

## virtualenv and virtualenvwrapper
Use pre-installed Python 3, includes virtualenv.  
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

### deactivate
    deactivate

### re-activate
If using virtualenvwrapper, can use command workon
    workon mysite

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

## Create app
    (mysite)➜  mysite git:(master) python manage.py startapp polls

## start development server
For production use a different server.
    $ python manage.py runserver

## Change model
3 steps
- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

## makemigrations
    (mysite)➜  polls git:(master) python manage.py makemigrations polls
    Migrations for 'polls':
      0001_initial.py:
        - Create model Choice
        - Create model Question
        - Add field question to choice

## sqlmigrate
Doesn't run migration, just prints to terminal

    (mysite)➜  polls git:(master) python manage.py sqlmigrate polls 0001
    BEGIN;
    CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL);
    CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
    CREATE TABLE "polls_choice__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "polls_question" ("id"));
    INSERT INTO "polls_choice__new" ("choice_text", "id", "votes") SELECT "choice_text", "id", "votes" FROM "polls_choice";
    DROP TABLE "polls_choice";
    ALTER TABLE "polls_choice__new" RENAME TO "polls_choice";
    CREATE INDEX polls_choice_7aa0f6ee ON "polls_choice" ("question_id");

## check
    (mysite)➜  polls git:(master) python manage.py check
    System check identified no issues (0 silenced).

## migrate
    (mysite)➜  polls git:(master) ✗ python manage.py migrate
    Operations to perform:
    Apply all migrations: auth, sessions, admin, contenttypes, polls
    Running migrations:
    Applying polls.0001_initial... OK

## Part 2 Playing with the API

### Add username and password (see keychain)
    python manage.py createsuperuser

### Customizing your project's templates

Get environment path to django
    (mysite)➜  polls git:(master) ✗ python -c "
    dquote> import sys
    dquote> sys.path = sys.path[1:]
    dquote> import django
    dquote> print(django.__path__)"

    ['/Users/stevebaker/.virtualenvs/mysite/lib/python3.4/site-packages/django']

Copy file base_site.html from django
django/contrib/admin/templates/admin/base_site.html

In project make directory templates/admin and add base_site.html.

In base_site.html change header from default 'Django administration' to Polls administration.
Tutorial notes:
"We use this approach to teach you how to override templates.
In an actual project, you would probably use the django.contrib.admin.AdminSite.site_header attribute
to more easily make this particular customization."

In base_site.html I changed back to original.
{{ site_header|default:_('Django administration') }}
Then in urls.py set admin.site_header

### Test
In file polls/polls/tests.py add
class QuestionMethodTests(TestCase): with method
def test_was_published_recently_with_future_question(self):

    ➜  polls git:(master) ✗ workon mysite
    (mysite)➜  polls git:(master) ✗ pwd
    /Users/stevebaker/Documents/projects/pythonProjects/django-projects/polls
    (mysite)➜  polls git:(master) ✗ ls
    README.md  db.sqlite3 manage.py  mysite     polls      templates

    (mysite)➜  polls git:(master) ✗ python manage.py test polls
    Creating test database for alias 'default'...
    F
    ======================================================================
    FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionMethodTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/stevebaker/Documents/projects/pythonProjects/django-projects/polls/polls/tests.py", line 20, in test_was_published_recently_with_future_question
        self.assertEqual(future_question.was_published_recently(), False)
    AssertionError: True != False

    ----------------------------------------------------------------------
    Ran 1 test in 0.002s

    FAILED (failures=1)
    Destroying test database for alias 'default'...
