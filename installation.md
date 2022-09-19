# Installation Process
## Virtual Environment
1. in the terminal type -> py -m venv <environment_name> 
2. cd into the <environment_name>  folder
3. in the terminal type -> Scripts\activate.bat
## Django Setup
4. in the terminal type -> pip install django
5. in the terminal type -> django-admin startproject <project_name>
6. cd into the <project_name> folder
7. in the terminal type -> django-admin startapp <app_name>
8. in the setting.py file add the app to INSTALLED APPS -> '<app_name>.apps.<appName>Config'
9. Migrate Project -> python manage.py migrate
10. Run server with -> py manage.py runserver
## Admin setup
11. Create super user ->  python manage.py createsuperuser
