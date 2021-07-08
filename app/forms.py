from app.models import Contact, Report
from django import forms
from django.forms.fields import IntegerField


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'messages')

class ReportForm(forms.Modelform):
    class Meta:
        model = Report
        fields = ('feedbackfor', 'message', 'rating')