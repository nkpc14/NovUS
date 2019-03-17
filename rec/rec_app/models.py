from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Skills(models.Model):
    name_skills = models.CharField(max_length=500)

    def __str__(self):
        return self.name_skills


class Hostel(models.Model):
    name_hostel = models.CharField(max_length=100)

    def __str__(self):
        return self.name_hostel


class Block(models.Model):
    name_block = models.CharField(max_length=100)

    def __str__(self):
        return self.name_block


class Department(models.Model):
    name_department = models.CharField(max_length=500)

    def __str__(self):
        return self.name_department


class Interest(models.Model):
    name_interest = models.CharField(max_length=500)

    def __str__(self):
        return self.name_interest


class Recruitment(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.IntegerField(
        validators=[RegexValidator(r'\d{8,8}',
                                   'Registration Number must be 8 digits', 'Invalid Registration Number')])
    phone = models.IntegerField(
        validators=[RegexValidator(r'\d{10,10}',
                                   'Number must be 10 digits', 'Invalid number')])
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.SET_NULL, null=True)
    block = models.ForeignKey(Block, on_delete=models.SET_NULL, null=True)
    room_no = models.IntegerField(validators=[RegexValidator(r'\d{1,5}')])
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    cgpa = models.FloatField(null=False, blank=False, default=None)
    interest = models.ForeignKey(Interest, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(validators=[RegexValidator(r'\d{4,4}')])

    def __str__(self):
        return self.name
