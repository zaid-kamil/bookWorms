from app.models import Author, Book, Contact, Genre, Report, Request
from django.contrib import admin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','display_genre')
    list_filter = ('status','author')   

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(Genre)
admin.site.register(Contact)
admin.site.register(Report)
admin.site.register(Request)