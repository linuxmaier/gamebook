from django.db import models

# Create your models here.
class GameBook(models.Model):
    title = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    author = models.ForeignKey('Author', related_name='gamebooks')
    pub_date = models.DateTimeField('date published')
    genre = models.CharField(max_length=50, default='unlisted')
    synposis = models.TextField()
    playthroughs = models.IntegerField()

    def __unicode__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_addr = models.EmailField(max_length=254)
    bio = models.TextField()

    def __unicode__(self):
        return self.first_name + self.last_name


class Page(models.Model):
    gamebook = models.ForeignKey('GameBook', related_name='pages')
    number = models.IntegerField()
    content = models.TextField()

    def __unicode__(self):
        return self.number


class Choice(models.Model):
    page_from = models.ForeignKey('Page', related_name='choices')
    page_to = models.ForeignKey('Page', related_name='choice_to_here')
    content = models.TextField()

    def __unicode__(self):
        return self.content
