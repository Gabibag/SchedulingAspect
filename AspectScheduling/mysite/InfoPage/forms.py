from django import forms
from django.utils.safestring import mark_safe


    
        
class LoginForm(forms.Form):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.label_suffix = " "  # Removes : as label suffix
  login = forms.CharField(label=' ', widget=forms.TextInput(
      attrs={'placeholder': 'ID Number', 'class': 'passwd', 'style': 'height: 25px;'}))
  
  password = forms.CharField(label=mark_safe('<br /> '),
                              widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'passwd', 'style': 'height: 25px;'}))
