from django.contrib import admin
from gamebook.models import GameBook, Author, Page, Choice


class PageInline(admin.TabularInline):
    model = Page


class GameBookAdmin(admin.ModelAdmin):
    inlines = [
        PageInline,
    ]
    fieldsets = [
        (None,          {'fields': ['title', 'active']}),
        ('Publication', {'fields': ['author', 'pub_date', 'genre']}),
        ('Content',     {'fields': ['synopsis', 'playthroughs']}),
    ]
    readonly_fields = ('playthroughs',)


admin.site.register(Author)
admin.site.register(GameBook, GameBookAdmin)
admin.site.register(Page)
admin.site.register(Choice)

