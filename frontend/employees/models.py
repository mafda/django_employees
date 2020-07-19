from django.db import models


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    document = models.IntegerField(unique=True)
    name = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    salary = models.FloatField()

    def _str_(self):
        return (
            f"       id: {self.employee_id}\n"
            f"full name: {self.name} {self.lastname}\n"
            f" document: {self.document}\n"
            f"   salary: {self.salary}\n"
        )
