from django.db import models

# Create your models here.


class Table(models.Model):
    si_no = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    parent_id = models.IntegerField(null=True)

    class Meta:
        ordering = ['si_no']
