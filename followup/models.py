from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    picture_url = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=100)
    grade = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.full_name


class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateTimeField("Attendance date")
    was_available = models.BooleanField(default=False)
    remark = models.CharField(max_length=200, blank=True)
    is_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.remark


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ministry = models.CharField(max_length=100, blank=True)
    assigned_numof_individuals = models.IntegerField(blank=True)
    