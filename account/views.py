from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import User

#定义表单模型
class UserForm(forms.Form):
    realname = forms.CharField(label='usrrealname',max_length=100)
    username = forms.CharField(label='usrusername',max_length=100)
    password = forms.CharField(label='usrpassword',widget=forms.PasswordInput())
    email = forms.EmailField(label='usremail')
    repeatpassword = forms.CharField(label='usrrepeatpassword',widget=forms.PasswordInput())


# Create your views here.
def sign_up(request):
    #if not request.method == 'POST':
        #return HttpResponse('error post')
    if request.method == 'POST':
    	form = UserForm(request.POST)
    	if form.is_valid():
            #获取表单信息
            new_realname = UserForm.cleaned_data['usrrealname']
            new_username = UserForm.cleaned_data['usrusername']
            new_password = UserForm.cleaned_data['usrpassword']
            new_email = UserForm.cleaned_data['usremail']

            if password and repeatpassword and password != repeatpassword:
                return HttpResponse('error password')
            else:

                User = Users.objects.create(
                    realname = new_realname,
                    username = new_username,
                    password = new_password,
                    email = new_email,
                    )

                User.save()
                return render_to_response('account/success.html',{'Form':UserForm})
    else:
        return render_to_response('account/sign_up.html',{'Form':UserForm})

    