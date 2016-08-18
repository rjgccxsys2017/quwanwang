from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .forms import UserForm
#from .models import User


def sign_up(request):
    #if not request.method == 'POST':
       # return HttpResponse('error post')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            new_realname = request.POST['userrealname']
            new_username = request.POST['usrusername']
            new_password = request.POST['usrpassword']
            new_repeatpassword = request.POST['usrrepeatpassword']
            new_email = requset.POST['usremail']


            user.set_realname(new_realname)
            user.set_username(new_username)
            user.set_password(new_password)
            user.set_email(new_email)
            user.save()
            
            return render(request,'account/success.html',{'form':UserForm})

    else:
        return render(request,'account/sign_up.html',{'form':UserForm})