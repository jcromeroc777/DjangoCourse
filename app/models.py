from django.db import models

# Create your models here.
class Cars(models.Model):
    brand = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)

    def __str__(self):
        return f'{self.brand} - {self.year}'

class Publisher (models.Model):
    name = models.TextField(max_length=250)
    address = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} - {self.address}'

class Author (models.Model):
    name = models.TextField(max_length=250)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Profile (models.Model):
    website = models.URLField()
    bio = models.TextField(max_length=250)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class Book (models.Model):
    title = models.TextField(max_length=250)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='authors')

    def __str__(self):
        return self.title
