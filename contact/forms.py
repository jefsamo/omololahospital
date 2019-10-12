from django import forms
from contact.models import Contact
# from contact.models import contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'from_email', 'phone_number', 'subject', 'message']

