from django.db import models

class competance(models.Model):
    comp=models.CharField(max_length=100)
    niveau=models.IntegerField()
    type=models.CharField(max_length=100)
    def __str__(self) -> str:
            return self.comp


class stage(models.Model):
    date=models.DateField()
    lieu=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    def __str__(self) -> str:
            return self.type

class Type(models.Model):
    nomType=models.CharField(max_length=100)  

class formation(models.Model):
    date=models.CharField(max_length=100)
    lieu=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    speci=models.CharField(max_length=100)
    type=models.ForeignKey('Type',on_delete=models.CASCADE,)
    

