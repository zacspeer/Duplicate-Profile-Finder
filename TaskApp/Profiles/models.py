from operator import mod
from statistics import mode
from django import forms
from django.db import models
from django import db
from django.forms import CharField, DateField, EmailField, IntegerField

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=120)
    last_name = models.CharField(blank=False, null=False, max_length=120)
    email = models.EmailField(blank=False, null=False)
    date_of_birth = models.DateField(blank=True, null=True)  # format will be YYYY-MM-DD
    class_year = models.IntegerField(blank=True, null=True)

    # def set_values(self, firstname, lastname, classyear, dob, email):
    #     self.first_name = firstname
    #     self.last_name = lastname
    #     self.date_of_birth = dob
    #     self.class_year = classyear
    #     self.email_field = email
