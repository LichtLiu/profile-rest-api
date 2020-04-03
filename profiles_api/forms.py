from django import forms
from .serializers import HelloSerializer

class HelloSerializerForm(forms.ModelForm):

    class Meta:
        model = HelloSerializer
        fields = ['name', 'date']

    date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y')
    )