from django.contrib import admin
from contact.models import Contact
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class ContactAdmin(UserAdmin):
    list_display = ('name', 'from_email', 'phone_number', 'subject', 'message')
    search_fields = ('name', 'from_email', 'phone_number', 'subject', 'message')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Contact)
