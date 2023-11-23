from django.db import models
import datetime
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

# Create your models here.

class Division(models.Model):
    divisionId = models.AutoField(primary_key=True)
    divisionName = models.CharField(max_length=500)

    def __str__(self):
        return self.divisionName

class Position(models.Model):
    positionId = models.AutoField(primary_key=True)
    devision = models.ForeignKey(Division, on_delete=models.CASCADE)
    posisitionName = models.CharField(max_length=100)

    def __str__(self):
        return self.posisitionName
    

GENDER = (
    ('F', 'F'),
    ('M', 'M'),
)

class Employees(models.Model):
    employeesId = models.AutoField(primary_key=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(max_length=10)
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(max_length=1, choices=GENDER)
    join_date = models.DateField(max_length=10)

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    @property
    def workper(self):
        #return int((datetime.now().date() - self.join_date).days / 30)
        today = datetime.now().date()

        delta = relativedelta(today, self.join_date)
        months = delta.years * 12 + delta.months
        years = delta.years

        result = f"{years} tahun {months % 12} bulan"
        return result