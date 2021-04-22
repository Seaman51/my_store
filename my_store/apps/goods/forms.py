from django.forms import ModelForm, TextInput, Textarea, DateInput, DateTimeInput, TimeInput
from .models import Good


class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = '__all__'
        widgets = {
            "good_name": TextInput(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(GoodForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if isinstance(field.widget, TextInput) or \
                    isinstance(field.widget, Textarea) or \
                    isinstance(field.widget, DateInput) or \
                    isinstance(field.widget, DateTimeInput) or \
                    isinstance(field.widget, TimeInput):
                field.widget.attrs.update({'placeholder': field.label})
