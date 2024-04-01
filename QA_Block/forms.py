from django import forms
from django.conf import settings
from QA_Block.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        if hasattr(settings, 'QA_DESCRIPTION_OPTIONAL'):
            self.fields['description'].required = not settings.QA_DESCRIPTION_OPTIONAL
