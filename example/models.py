from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=20, blank=True)
    date_created = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.name 
    

class Language(models.Model):
    name = models.CharField(max_length=20, blank=True)
    creator = models.CharField(max_length = 20, blank=True)
    paradigm = models.CharField(max_length=20, blank=True)
    date_created = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.name 

class Programmer(models.Model):
    name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name 