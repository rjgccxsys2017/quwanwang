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
	return render(request,'lists/about_us.html')

def blog(request):
	return render(request,'lists/blog.html')

def blog_post(request):
	return render(request,'lists/blog_post.html')

def blog_post1(request):
	return render(request,'lists/blog_post1.html')

def blog_post2(request):
	return render(request,'lists/blog_post2.html')

def coming_soon(request):
	return render(request,'lists/coming_soon.html')

def contact_us(request):
	return render(request,'lists/contact_us.html')

def error_page(request):
	return render(request,'lists/error_page.html')

def center(request):
	return render(request,'lists/help_center.html')

def item(request):
	return render(request,'lists/help_item.html')

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
	return render(request,'lists/shop_item.html')

def shopping_cart(request):
	return render(request,'lists/shopping_cart.html')

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
	return render(request,'lists/user_profile.html')

def portfolio(request):
	return render(request,'lists/portfolio.html')

def portfolio_item_1(request):
	return render(request,'lists/portfolio_item_1.html')

def portfolio_item_2(request):
	return render(request,'lists/portfolio_item_2.html')
	
def portfolio_item_3(request):
	return render(request,'lists/portfolio_item_3.html')
	
def portfolio_item_4(request):
	return render(request,'lists/portfolio_item_4.html')
	
def portfolio_item_5(request):
	return render(request,'lists/portfolio_item_5.html')
	
def portfolio_item_6(request):
	return render(request,'lists/portfolio_item_6.html')
	
def portfolio_item_7(request):
	return render(request,'lists/portfolio_item_7.html')
	
def portfolio_item_8(request):
	return render(request,'lists/portfolio_item_8.html')
	
def portfolio_item_9(request):
	return render(request,'lists/portfolio_item_9.html')
	
def portfolio_item_10(request):
	return render(request,'lists/portfolio_item_10.html')
	
def portfolio_item_11(request):
	return render(request,'lists/portfolio_item_11.html')
	
def portfolio_item_12(request):
	return render(request,'lists/portfolio_item_12.html')
	
def university(request):
	return render(request,'lists/university.html')
	
def user_profile_myemail(request):
	return render(request,'lists/user_profile_myemail.html')
	
def user_profile_mymessage(request):
	return render(request,'lists/user_profile_mymessage.html')
	
def xiaoyuan(request):
	return render(request,'lists/xiaoyuan.html')

def shipin(request):
	return render(request,'lists/shipin.html')
	