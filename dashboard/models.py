from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Notes"
        verbose_name_plural = "Notes"
        
    def __str__(self):
        return self.title

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class UpdateProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    institution = models.CharField(max_length=30)
    semester = models.CharField(null = True, max_length=2)
    bloodgroup = models.CharField(null = True, max_length=3)

    def __str__(self):
        return self.name