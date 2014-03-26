from django.contrib import admin
from gamebook.models import GameBook, Author, Page, Choice


class PageInline(admin.TabularInline):
    model = Page


class GameBookAdmin(admin.ModelAdmin):
    inlines = [
        PageInline,
    ]


admin.site.register(Author)
admin.site.register(GameBook, GameBookAdmin)
admin.site.register(Page)
admin.site.register(Choice)

