**Project Setup Instructions**
- clone the repository
- make a virtualenvironment

*command to create venv*
- python -m venv venv (name anything).
- venv/scripts/activate (for windows)
- source venv/bin/activate (for mac and linux)

- Install Requirements (pip3 install -r requirements.txt)
- setup the database for yourself. Currently Postgresdb is being used. change the NAME,USER, PASSWORD and HOST(if host is you localhost then leave it) in your settings.py file.
- Use Python manage.py migrate command to reflect the tables in your db
- There you go start your development server with (python manage.py runserver)