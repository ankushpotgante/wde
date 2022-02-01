from django.db import models

# Create your models here.

class Feedback(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.CharField(max_length=800)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    