from django import forms
from . import models


class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = models.ForumMessage
        fields = ('content', 'attached_file')

        labels = {
            'content': 'Содержание',
            'attached_file': "Прикрепить файл"
        }
        widgets = {
            'content': forms.Textarea( attrs={"rows": 16, "cols": 64} ),
            'attached_file': forms.widgets.FileInput()
        }
