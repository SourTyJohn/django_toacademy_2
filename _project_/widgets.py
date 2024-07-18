from django.forms.widgets import DateInput as baseDateInput


class DateInput(baseDateInput):
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('min', '1900-01-01')
        self.attrs.setdefault('max', '2100-01-01')
