from django.db import models

from django.db import models

class Employees(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    job_title=models.CharField(max_length=255)
    salary=models.IntegerField()

    def __str__(self):
        return str(self.id)

