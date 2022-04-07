# Workspace Organization


All files for the project will be stored in the Github repository cs3450group2. Documentation, including the project plan, definition of requirements, and use case diagrams, are to be included in the /docs/ folder in this repository. Sprint planning documents and reports can be found in the /sprints/ folder.


# Version control procedures


To keep track of work done on issues, this repository creates issue branches for each issue opened in Github. Pull requests are reviewed by at least one other member of the team before being merged into the main branch to avoid merging bad code.


# Tool stack description and setup procedure


Django is a convenient framework for this app since it comes with a simple SQLite database. This app will be using database features to manage many different types of data making SQLite very useful. Django also uses the Python language which will help with team functionality since we all know the language.


## Build instructions
install Django

`pip install Django"


Clone project from github using the command


`bash $ git clone git@github.com:cs3450group2/group2.git`


Migrate in bash


`bash $ python manage.py migrate`


Create an admin account


`bash $ python manage.py createsuperuser`


Then complete migrations


`bash $ python manage.py makemigrations`


Then migrate again


`bash $ python manage.py migrate`

runserver then access admin site
`bash $ python manage.py runserver`
`localhost:8000/admin`

manually create an owner user

`to do this you must access the admin server and create a user, then create a userProfile with a type of "owner", all lowercase. Once you have created it, make sure the userProfile is assigned to the user you just created so they link in a 1-1 relationship.`

and finally logout of admin website and you should be good to go

# Unit testing instructions


Unit tests are contained in the tests.py file in the repository. These can be run by entering the repository then typing the following:

`bash $ python manage.py test`

