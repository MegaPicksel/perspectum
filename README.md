Perspectum task:
================
This application allows users to register, login and upload files, and logout.

To set this application up on your local machine, you will need the following technologies:
-------------------------------------------------------------------------------------------
* Python 3
* Django 2.0
* Virtualenv (Virtual Environment)

The downlaod for python3 is system dependent. To download python 3: https://www.python.org/downloads/

If you have not got pip (Python Installer Package), you will need to download it. The download is system dependent, see the official 
documentation here: https://pip.pypa.io/en/stable/installing/

Note:
-----
If you are using a Linux distro, or a Unix-like OS (All Apple computers, BSD), your machine comes pre-installed with a python 2.7 interpreter.
Your computer will automatically use this python interpreter and NOT a python 3 interpreter, even if you have installed one, this might cause 
unexpected behaviour. Further more, some systems rely on python 2.7, so DO NOT attempt to delete it.

To Use Python 3 on a Linux, or Unix-like computer you will need to set up a virtual environement:
To Install virtualenv:
* pip3 install virtualenv or (windows users) pip install virtualenv

To start virtualenv:
* virtualenv "project name"

Then enter the project directory and type: source bin/activate.
You will know that the environemnt is activate because your command line will change, the virtualenv name will be in brackets in front of everython else.
When you are finished working and would like to deativate type: deactivate

To Download Django:
* pip3 install django or pip install django

Once the dowload has completed, clone this repository to your computer. Copy the files from the folder on your computer into the virtualenv.
You will be notified of existing files with the same name, overwrite them.

In order to start the project:
------------------------------
Python manage.py runserver

To migrate database and set up an admin user:
----------------------------------------------
Python manage.py makemigrations
python manage.py migrate

python manage.py makemigrations

If you need assistance, see the django documentation: https://docs.djangoproject.com/en/2.1/
