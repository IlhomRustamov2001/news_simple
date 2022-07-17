from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):#user uchun formani fieldlari bilan yaratebmiz
    class Meta(UserCreationForm):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('age', 'address', 'job')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=CustomUser
        fields=UserChangeForm.Meta.fields