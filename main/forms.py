from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user']
        fields = '__all__'
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
        }

from .models import RefurbishedLaptop

class RefurbishedLaptopForm(forms.ModelForm):
    available = forms.TypedChoiceField(
        choices=((True, 'Yes'), (False, 'No')),
        coerce=lambda x: x == 'True',
        widget=forms.Select
    )
    class Meta:
        model = RefurbishedLaptop
        fields = '__all__'