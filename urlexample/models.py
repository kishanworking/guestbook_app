from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=20, blank=True)
    date_created = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.title
    

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100, blank=True)
    order = models.IntegerField(blank=True, null=True)
    date_created = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.title

class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100, blank=True)
    order = models.IntegerField(blank=True, null=True)
    code_link = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length = 100, blank=True)
    
    def __str__(self):
        return self.title 