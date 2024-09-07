from django import forms


class SaveValidFormMixin:
    def form_valid(self, form: forms.ModelForm):
        form.save()
        return super(SaveValidFormMixin, self).form_valid(form)
