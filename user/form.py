from django import forms


class userForm(forms.Form):
	name = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput,max_length=50)
	password_re = forms.CharField(max_length=50 ,widget=forms.PasswordInput)