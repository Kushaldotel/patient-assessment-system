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

**Assumptions Made Duing Development**

- Clinicians will use the system
- Our system user will be the clinicians
- Patients record will be kept in a Patient Db by clinicians
- Assessment record for a Patient will be kept in a Assessment Db
- Clinician must be able to create a new Patient record
- Clinician must be able to create Assessment record for his existing patients
- Clinicians must be able to create a new patient and assessment detail at the same time is that patient doesnot exist in their database
- A clinician must not be able to get,update or destroy other patients detail that donesnot belong to them

**Project Challanges**
- Easy and simple project no challanges faced

**Additional features**
- Verification of patient record if they belong to a clinic
- Added more reasonable fields in the Database Tables
- Implemented the data isolation for each clinicians.
- Made Customuser model to assure data isolation rather than using django-tenants.
- Implemented cors_headers to listen from localhost:3000 for now too

**Deployement in Aws can Look like**

- Login into your aws account
- just make a security group with inbound rules from ssh, http and https
- now create an ec2 instance(use linux os and security group just created) and like connect to it
- update and upgrade the instance
- Install python virtualenv package
- Create the virtual env
- activate the virtualenvironment
- Clone the repo (if private generate key and add to your github account under ssh and gpg keys)
- install the requirementsfile
- change the debug to false in production
- install supervisor for management
- install gunicorn using pip
- install nginx in your instance
- configure gunicorn this will create a app.sock file give name
- user supervisor to reread and update
- configure the nginx for django configuration. Listen to your app.sock port 80. Add your ec2 ip
- reload nginx after a successful addition
- you can like set allowed host in your settings.py too.
- If you have domain set the A record for your ec2 ip and change the nginx config for your django project and like set in allowed host in settings.py too.
- Save and reload nginx

For CI/CD we can use github Actions