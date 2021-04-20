from django.db import models

# Create your models here.

class Book(models.Model):
    book_title=models.CharField(max_length=100)
    author=models.CharField(max_length=250)
    publisher=models.CharField(max_length=250)
    summary=models.CharField(max_length=90000)
    Isbn=models.CharField(max_length=13)
    location=models.CharField(max_length=10)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.book_title + '-' +self.author