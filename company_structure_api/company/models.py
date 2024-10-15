from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    @property
    def employee_count(self):
        return self.employees.count()

    @property
    def total_salary(self):
        return self.employees.aggregate(models.Sum('salary'))['salary__sum'] or 0


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, db_index=True)
    photo = models.ImageField(upload_to='photos/')
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return f"id={self.id} first_name={self.first_name} last_name={self.last_name} department={self.department.id}"
