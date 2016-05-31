from django import forms
from django.core.exceptions import ValidationError


def validate_rating(value):
    if value < 1 or value > 10:
        raise ValidationError(u'Rating should be between 1 and 10')


class CommentForm(forms.Form):
    text = forms.CharField(max_length=500, widget=forms.Textarea, required=False)
    rating = forms.IntegerField(validators=[validate_rating], required=True)
