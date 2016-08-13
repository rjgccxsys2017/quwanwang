"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin
from lists.views import about_us,blog,blog_post,blog_post1,blog_post2
from lists.views import coming_soon,contact_us,error_page,center,item
from lists.views import home,shop,shop_item,shopping_cart,sign_in,user_profile
from account.views import sign_up,UserForm


urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^about_us/$',about_us,name = 'about_us'),
    url(r'^blog/$',blog,name = 'blog'),
    url(r'^blog_post/$',blog_post,name = 'blog_post'),
    url(r'^blog_post1/$',blog_post1,name = 'blog_post1'),
    url(r'^blog_post2/$',blog_post2,name = 'blog_post2'),
    url(r'^coming_soon/$',coming_soon,name = 'coming_soon'),
    url(r'^contact_us/$',contact_us,name = 'contact_us'),
    url(r'^error_page/$',error_page,name = 'error_page'),
    url(r'^help_center/$',center,name = 'center'),
    url(r'^help_item/$',item,name = 'item'),
    url(r'^$',home,name = 'home'),
    url(r'^shop/$',shop,name = 'shop'),
    url(r'^shop_item/$',shop_item,name = 'shop_item'),
    url(r'^shopping_cart/$',shopping_cart,name = 'shopping_cart'),
    url(r'^sign_in/$',sign_in,name = 'sign_in'),
    url(r'^sign_up/$',sign_up,name = 'sign_up'),
    url(r'^user_profile/$',user_profile,name = 'user_profile'),
)
