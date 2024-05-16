from django import forms


class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=500
    )
    email = forms.EmailField()
    password = forms.PasswordInput()


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
