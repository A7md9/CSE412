# CSE412
# Group 36: Ghaida Almalki, Ash Sharma, Ahmed Alyahya, Faisal Aloraini

# Library Management System
Description:
An easy-to-use program called a library management system is created to manage a library's operations. It has features like categorizing books, following borrowing and returning them, controlling user accounts, and producing reports.

How to setup the project
1- Set Up a Virtual Environment
To isolate your project dependencies:
python3 -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
2- Install Required Packages
Using the provided requirements.txt:
pip install -r requirements.txt
3- Configure the Database
Ensure the SQLite file is in the appropriate location or will be created automatically.
4- Run Migrations
To create or update necessary database tables:
python manage.py migrate
5- Create a Superuser
To access the admin panel:
python manage.py createsuperuser
6- Start the server : 
python manage.py runserver
Post-Installation
Accessing the Admin Panel
Navigate to http://localhost:8000/admin/ and log in using the superuser credentials 
