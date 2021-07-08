from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateTimeField, EmailField, IntegerField, TextField
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.core.validators import RegexValidator,MinValueValidator,MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name

class Book(models.Model):

    STATUS = (
        ('a', 'Available'),
        ('s', 'Shared'),
    )
    user = models.ForeignKey(User,on_delete=CASCADE)
    title = CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    summary = TextField(max_length=1000, help_text='Enter a brief description of the book')
    book_state = CharField(max_length=255,default="old")
    is_signed_by_author = BooleanField("is book signed by Author?",default=False)
    is_collection = BooleanField("is part of collection",default=False)
    image = ImageField("Main Image",upload_to="books",default="book_default.png")
    image2 = ImageField("image 2",upload_to="books",blank=True,null=True)
    image3 = ImageField("image 3",upload_to="books",blank=True,null=True)
    status = models.CharField(max_length=1,choices=STATUS,blank=True,default='a',help_text='Book availability',)
    date =DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class BookShare(models.Model):

    SHARE_TYPE = (
        ('p', 'Permanent'),
        ('t', 'Time based Share'),
    )
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    share_to_user= models.ForeignKey(User,on_delete=models.DO_NOTHING)
    sharing_type = models.CharField(max_length=1,choices=SHARE_TYPE,blank=True,default='p',help_text='Book availability',)
    due_back = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ['due_back','sharing_type']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'


class Contact(models.Model):
    """Model definition for Contact."""

    name = CharField(max_length=30)
    email =EmailField()
    subject = CharField(max_length=255)
    messages = TextField()
    
    class Meta:
        """Meta definition for Contact."""
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name

class Report(models.Model):
    class Feedback_options(models.TextChoices):
        COMPLAIN='CMP',_('complain')
        REVIEW='REV',_('review')
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    feedbackfor = models.CharField(max_length=15, choices=Feedback_options.choices,default=Feedback_options.REVIEW)
    message = models.CharField(max_length=100,)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],help_text="give a rating between 1 to 5")