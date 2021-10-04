from django import forms 


class LoginForm(forms.Form):
    username = forms.CharField(max_length=19)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=19)
    display_name = forms.CharField(max_length=19)
    password = forms.CharField(widget=forms.PasswordInput)
    



