from django import forms
from django.utils.safestring import mark_safe
class LoginForm(forms.Form):
    login = forms.CharField(label='ID Number')
    
    password = forms.CharField(label=mark_safe('<br /> Password'),
        widget=forms.PasswordInput(attrs={'class': 'passwd'}))
