from django import forms

class UserForm(forms.Form):
	realname = forms.CharField(label='usrrealname',max_length=100)
	username = forms.CharField(label='usrusername',max_length=100)
	password = forms.CharField(label='usrpassword',widget=forms.PasswordInput())
	email = forms.EmailField(label='usremail')
	repeatpassword = forms.CharField(label='usrrepeatpassword',widget=forms.PasswordInput())

