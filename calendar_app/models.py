from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=600)
    start_time = models.DateTimeField()
    end_tie = models.DateTimeField()



    def __str__(self):
        return f"{self.title}"

    @property
    def get_html_url(self):
        url = reverse('cal:event-edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'