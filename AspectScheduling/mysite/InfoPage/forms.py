from django import forms

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'passwd'}))
