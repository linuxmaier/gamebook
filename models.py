from django.db import models

# Create your models here.
class GameBook(models.Model):
    title = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    author = models.ForeignKey('Author', related_name='gamebooks')
    pub_date = models.DateTimeField('date published')
    genre = models.CharField(max_length=50, default='unlisted')
    synopsis = models.TextField()
    playthroughs = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def new_page(self, page_text):
        page_count = self.pages.count()
        return Page(gamebook=self, number=page_count + 1, content=page_text)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_addr = models.EmailField(max_length=254)
    bio = models.TextField()

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Page(models.Model):
    gamebook = models.ForeignKey('GameBook', related_name='pages')
    number = models.IntegerField()
    content = models.TextField()

    def __unicode__(self):
        return str(self.number) + " in " + self.gamebook.title

    def new_choice(self, text_content, target_num):
        return Choice(page_from=self, page_to=target_num, content=text_content)


class Choice(models.Model):
    page_from = models.ForeignKey('Page', related_name='choices')
    page_to = models.IntegerField()
    content = models.TextField()

    def __unicode__(self):
        return "Go to page " + str(self.page_to)
