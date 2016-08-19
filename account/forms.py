from django import forms
from django.db import models
from account.models import User
class UserForm(forms.Form):
	realname = forms.CharField(label='realname',max_length=100)
	username = forms.CharField(label='username',max_length=100)
	password = forms.CharField(label='password',widget=forms.PasswordInput())
	email = forms.EmailField(label='email')
	repeatpassword = forms.CharField(label='repeatpassword',widget=forms.PasswordInput())

	class Meta:
		model = User