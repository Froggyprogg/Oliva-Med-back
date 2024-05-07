from django import forms
from django.conf import settings
from Oliva_pages.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'review_text']
