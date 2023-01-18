from django import forms

class CreateClassForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField()