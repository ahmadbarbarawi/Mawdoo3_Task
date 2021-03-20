import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RestApis.settings')
django.setup()
from apis.models import Employees
from faker import Faker


class fake_data:
    def __init__(self,number):
        self.num=number

    def create_employees(self):
        fake = Faker()
        number=self.num
        for i in range(number):
            print(i)
            first_name = fake.first_name()
            last_name = fake.last_name()
            job = fake.job()
            salary = fake.random_int(350, 1000, 50)
            employee = Employees(first_name=first_name, last_name=last_name, job_title=job, salary=salary)
            employee.save()
        return (1)




