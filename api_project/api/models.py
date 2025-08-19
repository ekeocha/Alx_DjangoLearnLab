from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField(null= True,blank= True)
    isbn = models.CharField(max_length=13, unique=True, default="0000000000000")

    def __str__(self):
        return self.title