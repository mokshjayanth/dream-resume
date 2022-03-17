from dataclasses import fields
from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class EduForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = (
            'duration',
            'course',
            'university',
            'place',
            'description',
        )

class ProForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'duration',
            'name',
            'programming_language',
            'description',
        )
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = (
            'name',
            'description',
            'certificate'
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username',)
        field_classes = {'username': UsernameField}