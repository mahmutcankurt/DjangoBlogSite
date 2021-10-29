from django import forms
from django.db.models import fields
from .models import *
from django.contrib.admin import widgets

class CustomAdminPageForm(forms.ModelForm):
    pass