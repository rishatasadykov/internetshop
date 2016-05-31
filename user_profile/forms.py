from django import forms
from models import UserProfile
from django.core.exceptions import ValidationError


class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    site = forms.URLField(required=False)


def validate_amount(amount):
    if amount < 1:
        raise ValidationError(u'Amount should be positive')


class TopUpForm(forms.Form):
    amount = forms.IntegerField(validators=[validate_amount], required=True)


class AvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar"]
