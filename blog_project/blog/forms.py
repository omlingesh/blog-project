from django import forms
from django.db import models
from django.forms import fields
class Email_Form(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
    
from blog.models import Comment
class Commentform(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')