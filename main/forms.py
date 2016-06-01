from django import forms
from good.models import currencies


class UserProfileForm(forms.Form):
    login = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    currency = forms.ChoiceField(currencies)
    avatar = forms.ImageField()


class LoginForm(forms.Form):
    login = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=50, required=True)