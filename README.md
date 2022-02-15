# Workspace Organization

All files for the project will be stored in the Github repository cs3450group2. Documentation, including the project plan, definition of requirements, and use case diagrams, are to be included in the /docs/ folder in this repository.

# Version control procedures

To keep track of work done on issues, this repository creates issue branches for each issue opened in Github. Pull requests are reviewed by at least one other member of the team before being merged into the main branch to avoid merging bad code.

# Tool stack description and setup procedure

Django is a convenient framework for this app since it comes with a simple SQLite database. This app will be using database features to manage many different types of data making SQLite very useful. Django also uses the Python language which will help with team functionality since we all know the language.

## Build instructions

- Clone project from github using the command

  - `bash $ git clone https://github.com/cs3450group2/milestone1.git`

- Create and start a virtual environment

  - `bash $ virtualenv --no-site-packages`

- Install the project dependencies

  - `bash $ pip install -r requirements.txt`

- Create a file named "secret.sh"

  - `bash $ touch secrets.sh`

- Obtain a secret from MiniWebTool key and add to secret.sh

  - `bash $ export SECRET_KEY='<secret_key>'`

- Add secret.sh to .gitignore file

- Create a postgres db and add the credentials to settings.py

```
DATABASES = {
   'default':  {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'db_name',
       'USER': 'name',
       'PASSWORD': '',
       'HOST': 'localhost',
       'PORT': '',
       }
   }
```

- Migrate in bash

  - `bash $ python manage.py migrate`

- Create an admin account

  - `bash $ python manage.py createsuperuser`

- Then complete migrations

  - `bash $ python manage.py makemigrations group2`

- Then migrate again

  - `bash $ python manage.py migrate`

- and finally

  - `bash $ python manage.py runserver`

Type `localhost:8000` in a browser to see the app running.

# Unit testing instructions

Unit tests are located in files prefixed with `test_`. Tests can be run by executing `./manage.py test`.

# System testing instructions

Start by running an instance of the web app by first entering the repository and then by entering the following:

`bash $ python manage.py runserver`

Now that the app is running, open an internet browser and enter the address `localhost:8000`

Login to the web app using the following credentials.

Username: SystemTest, Password: systest
