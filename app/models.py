from django.db import models

# Create your models here.
class Cars(models.Model):
    brand = models.TextField(max_length=250)

    def __str__(self):
        return self.name
