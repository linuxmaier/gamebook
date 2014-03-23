from django.db import models

# Create your models here.
class GameBook(models.Model):
    title = models.CharField(max_length=50)
    pub_date = modelsDateTimeField('date published')
    pages = models.


class Author(models.Model):
    full_name = models.CharField(max_length=50)
    email_addr = models.CharField(max_length=254)
    gamebooks = models.ForeignKey(GameBook, related_name='author')
    bio = models.TextField()

