from django import forms
from . import models


class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = models.ForumMessage
        fields = ('content', )

        labels = {
            'content': 'Содержание',
        }
        widgets = {
            'content': forms.Textarea(
                attrs={
                    "rows": 16,
                    "cols": 64
                }
            )
        }
