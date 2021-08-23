from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=600)
    start_time = models.DateTimeField()
    end_tie = models.DateTimeField()

    def __str__(self):
        return f"{title}"