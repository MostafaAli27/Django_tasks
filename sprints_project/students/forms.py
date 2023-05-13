from django import forms
from django.forms import ModelForm
from .models import Student , Course

class Student_form(ModelForm):
    class Meta:
        model=Student
        fields="__all__"