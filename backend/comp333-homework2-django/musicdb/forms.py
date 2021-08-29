from django.forms import ModelForm, CharField
from django import forms
from .models import Users, Years, Ratings


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']

class RetrieveRatingsForm(forms.Form):
    username = forms.CharField()

class RetrieveByYearForm(forms.Form):
    year = forms.IntegerField()


