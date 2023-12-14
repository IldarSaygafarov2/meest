from django import forms
from .models import UserRequest


class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = [
            'track_number',
            'fullname',
            'passport_series',
            'passport_number',
            'pinfl',
            'phone_number',
        ]
        widgets = {
            "track_number": forms.TextInput(attrs={
                'required': True,
                'placeholder': 'ACV000000000',
                'id': 'track-number',
                'oninput': "this.value = this.value.toUpperCase()",
            }),
            "fullname": forms.TextInput(attrs={
                'required': True,
                'placeholder': 'Иванов Иван Иванович'
            }),
            "passport_series": forms.TextInput(attrs={
                'required': True,
                'placeholder': 'AA',
                'class': 'passport__data-seria',
                'id': 'passport-seria',
                'oninput': "this.value = this.value.toUpperCase()",
                'title': 'Символы должны быть написаны на латинице'
            }),
            "passport_number": forms.TextInput(attrs={
                'required': True,
                'placeholder': '1234567',
                'class': 'passport__data-number',
                # 'pattern': '[0-9]{12}',
            }),
            "pinfl": forms.TextInput(attrs={
                'required': True,
                'placeholder': '12345678901234',
            }),
            "phone_number": forms.TextInput(attrs={
                'required': True,
                'placeholder': '998900000000',
                'value': '+998'
            }),
        }
