from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .forms import UserForm
from .models import User


def sign_up(request):
    #if not request.method == 'POST':
        #return HttpResponse('error post')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            new_realname = request.POST['realname']
            new_username = request.POST['username']
            new_password = request.POST['password']
            new_repeatpassword = request.POST['repeatpassword']
            new_email = request.POST['email']

            user = form.save()
            
            return render(request,'account/success.html',{'form':UserForm})

    else:
        return render(request,'account/sign_up.html',{'UserForm':UserForm})