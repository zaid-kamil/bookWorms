from app.models import Book
from django.contrib import admin

@admin.register(Book)
class addinstitute(admin.ModelAdmin):
    list_display = ('title','author','genre','category')
