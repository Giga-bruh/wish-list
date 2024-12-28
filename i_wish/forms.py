from i_wish import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Polzovatel

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Polzovatel
#         fields = ('username', 'email')

class Formi_add_zelanie(forms.ModelForm):
    class Meta:
        model=models.Zelanie
        fields=[
        "title" ,
        "description",
        "links",
        "image"
        ]
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Polzovatel
        fields = ('username', 'email')
