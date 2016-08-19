from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .forms import UserForm
from .models import User


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            realname = form.cleaned_data['realname']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeatpassword = form.cleaned_data['repeatpassword']
            email = form.cleaned_data['email']

            if password and repeatpassword and password != repeatpassword:
                return HttpResponse('Password ERROR')

            user = User()
            user.realname = realname
            user.username = username
            user.password = password
            user.email = email
            user.save()

            
            
            return render(request,'account/success.html',{'form':UserForm})

    else:
        return render(request,'account/sign_up.html',{'form':UserForm})