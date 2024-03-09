from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    completed = models.BooleanField(default="TRUE")
    added_date = models.DateTimeField(auto_now=True)
