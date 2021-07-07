from Tasks_app.settings import AUTH_PASSWORD_VALIDATORS
from django.core import validators
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.password_validation import validate_password
# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=200, unique=True, validators=[
                                RegexValidator(regex='^[a/A][a-zA-Z0-9]*[1/0]$', message="Please Ensure that username follows the convention", code="invalid_username")])
    join_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(
        max_length=100, validators=[validate_password])

    class Meta:
        ordering = ['uid']


class Tasks(models.Model):
    tid = models.AutoField(primary_key=True, unique=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(
        max_length=200, validators=[MinLengthValidator(4)])
    task_description = models.TextField(max_length=2000, null=True)
    task_pic = models.ImageField(null=True, blank=True)
    create_time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['tid']
