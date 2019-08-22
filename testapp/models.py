from django.db import models

class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=60)
    def __str__(self):
        return self.ename
# Create your models here.
