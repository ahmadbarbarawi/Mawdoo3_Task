# Mawdoo3_Task
This is the rest api task that I have implemented for Mawdoo3 company 
you need to download the source code in your machine 
you should install:
  1.python :FROM **https://www.python.org/**
  2.django: FROM **https://www.djangoproject.com/download/**
  3.restframework using this command: **pip install djangorestframework**
  4.faker using this command: **pip install faker**
then run the code using **python manage.py runserver **
there are a list of links :
{
    "List all employees": "/get_all_employees/",
    "List Employee by ID": "/get_employee_by_id/",
    "Create New Employee": "/create_new_employee/",
    "create_fake_data": "/generate_fake_data/"
}
1. **http://127.0.0.1:8000/apis/get_all_employees/** when you request this url it will respond with the list of all employees
2. **http://127.0.0.1:8000/apis/get_employee_by_id/[id]/** when you request this url you have to pass the employee id you want like this **/get_employee_by_id/1/** and it will respond with the specific employee
3. ***http://127.0.0.1:8000/apis/create_new_employee/** when you request this url you have to pass the data in valid **JSON format** and it will create a new employee
4. ***http://127.0.0.1:8000/apis/create_fake_data/[count]/** when you request this url it will fill the database with fake data. You should pass the number of employees you want, like this **/create_fake_data/20/**

Note that valuse between [] are inputed by the user 

 TO check the database request this url **http://127.0.0.1:8000/admin** username=admin password:admin
 
