from django import forms
from .models import EntradaCine
from django import forms
from .models import EntradaCine

class EntradaCineForm(forms.ModelForm):
    class Meta:
        model = EntradaCine
        fields = '__all__'
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'}),
            'Hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
