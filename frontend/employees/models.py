from django.db import models


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    document = models.IntegerField(unique=True)
    name = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    salary = models.FloatField()

    def __str__(self):
        return f"{self.name};{self.lastname};{self.document};{self.salary};"

