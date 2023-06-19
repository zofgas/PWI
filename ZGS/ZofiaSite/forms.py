from typing import Any
from django import forms
from .models import Mess
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MessForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   "placeholder": "Napisz coś o kwiatach",
                                   "class":"form-control",
                               }
                           ),
                           label="",
                           )
    class Meta:
        model = Mess
        exclude = ("user",)

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nazwa użytkownika'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Wymagania. 150 znaków lub mniej. Litery, cyfry i @/./+/-/_ tylko.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Nie uzywaj swoich danych personalnych w haśle.</li><li>Hasło musi zawierać minimum 8 znaków.</li><li>Nie uzywaj popularnych haseł</li><li>Hasło nie może być złożone tylko z cyfr</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Potwierdź hasło'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<ul class="form-text text-muted small"><li>Wpisz hasło jeszcze raz</li></ul>'