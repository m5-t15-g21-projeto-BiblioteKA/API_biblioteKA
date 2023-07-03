from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    book_genre = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=200)
    publishing_company = models.CharField(max_length=50)
    num_copies = models.IntegerField()
    
    users = models.ManyToManyField('users.User', related_name='books' )

