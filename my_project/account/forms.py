from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'user_name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'pass'}))