from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

class Book(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    title = CharField(max_length=255)
    author = CharField(max_length=255)
    genre = CharField(max_length=30)
    category = CharField(max_length=255,default="fantasy")
    book_state = CharField(max_length=255,default="old")
    is_signed_by_author = BooleanField("is book signed by Author?",default=False)
    is_collection = BooleanField("is part of collection",default=False)
    date =DateTimeField(auto_now=True)
    image = ImageField("Main Image",upload_to="books",default="book_default.png")
    image2 = ImageField("image 2",upload_to="books",blank=True,null=True)
    image3 = ImageField("image 3",upload_to="books",blank=True,null=True)
    is_shared = BooleanField(default=False)
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

