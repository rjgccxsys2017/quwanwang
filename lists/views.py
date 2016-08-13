from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import e_mailaddress
from django.core.urlresolvers import reverse

#class ContactForm(ModelForm):
	#class Meta:
		#model = e_mailaddress
		#fields = ('email')

def about_us(request):
	return render(request,'lists/about-us.html')

def blog(request):
	return render(request,'lists/blog.html')

def blog_post(request):
	return render(request,'lists/blog-post.html')

def blog_post1(request):
	return render(request,'lists/blog-post1.html')

def blog_post2(request):
	return render(request,'lists/blog-post2.html')

def coming_soon(request):
	return render(request,'lists/coming-soon.html')

def contact_us(request):
	return render(request,'lists/contact-us.html')

def error_page(request):
	return render(request,'lists/error-page.html')

def center(request):
	return render(request,'lists/help-center.html')

def item(request):
	return render(request,'lists/help-item.html')

def home(request):
	
	if request.method == 'POST':
		new_e_mailaddress = request.POST['e_mailaddress']
		e_mailaddress.objects.create(email = new_e_mailaddress)

	else:
		new_e_mailaddress = ''
	
	return render(request,'lists/index.html',{
		'new_e_mailaddress' : new_e_mailaddress
		})

	
def shop(request):
	return render(request,'lists/shop.html')

def shop_item(request):
	return render(request,'lists/shop-item.html')

def shopping_cart(request):
	return render(request,'lists/shopping-cart.html')

def sign_in(request):
	return render(request,'lists/sign_in.html')

#def sign_up(request):
	#if
	#request.method == 'POST':
		#post = request.POST
		#name1 = post['real_name']
		#name2 = post['nick_name']
		#email = post['accountemail']
		#password_1 = post['password1']
		#person.objects.create(real_name=name1,nick_name=name2,accountemail=email,psaaword1=password_1,password2=password_2)

		#try:
			#User.objects.create_user(
                #email = accountemail,
		        #password = password1,
		        #password1 =  password2,
		        #nick_name = nick_name,
		        #real_name = real_name,
           # )
		#except:
			#return HttpResponse('nick_name or email already be taken')
		#else:
			#return HttpResponse('OK')
	#else:
	#return render(request,'account/sign_up.html')

def user_profile(request):
	return render(request,'lists/user-profile.html')
