from django.contrib import admin
from gamebook.models import GameBook, Author, Page, Choice


admin.site.register(Author)
admin.site.register(GameBook)
admin.site.register(Page)
admin.site.register(Choice)

