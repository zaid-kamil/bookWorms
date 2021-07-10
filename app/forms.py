from django.forms.models import ModelForm
from app.models import Author, Book, BookShare, Contact, Report, Profile
from django import forms
from django.forms.fields import IntegerField
from django.forms import widgets


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'messages')

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('feedbackfor', 'message', 'rating')
        widgets ={
            'rating': widgets.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'summary', 'book_state', 'is_signed_by_author',
                  'is_collection', 'image','image2','image3')

class AuthorForm(ModelForm):       
    class Meta:       
        model = Author       
        fields = ('first_name', 'last_name')


class BookShareForm(ModelForm):
    class Meta:
        model = BookShare
        fields = ('book', 'share_to_user', 'sharing_type', 'due_back')
        


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('firstname','lastname','email','phone','gender','dob','photo','altcontact','address','city','pincode')
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker', 'id': 'data_input','type':'date'})
        }