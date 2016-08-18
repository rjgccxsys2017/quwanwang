"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  ##url(r'^$', views.home, name='home')
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
from lists.views import portfolio,portfolio_item_1,portfolio_item_2,portfolio_item_3,portfolio_item_4,portfolio_item_5
from lists.views import portfolio_item_6,portfolio_item_7,portfolio_item_8,portfolio_item_9,portfolio_item_10,portfolio_item_11,portfolio_item_12
from lists.views import university,user_profile_myemail,user_profile_mymessage,xiaoyuan,shipin
from account.views import sign_up


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
    url(r'^help_center/$',center,name = 'help_center'),
    url(r'^help_item/$',item,name = 'help_item'),
    url(r'^$',home,name = 'home'),
    url(r'^shop/$',shop,name = 'shop'),
    url(r'^shop_item/$',shop_item,name = 'shop_item'),
    url(r'^shopping_cart/$',shopping_cart,name = 'shopping_cart'),
    url(r'^sign_in/$',sign_in,name = 'sign_in'),
    url(r'^sign_up/$',sign_up,name = 'sign_up'),
    url(r'^user_profile/$',user_profile,name = 'user_profile'),
    url(r'^portfolio/$',portfolio,name = 'portfolio'),
    url(r'^portfolio_item_1/$',portfolio_item_1,name = 'portfolio_item_1'),
    url(r'^portfolio_item_2/$',portfolio_item_2,name = 'portfolio_item_2'),
    url(r'^portfolio_item_3/$',portfolio_item_3,name = 'portfolio_item_3'),
    url(r'^portfolio_item_4/$',portfolio_item_4,name = 'portfolio_item_4'),
    url(r'^portfolio_item_5/$',portfolio_item_5,name = 'portfolio_item_5'),
    url(r'^portfolio_item_6/$',portfolio_item_6,name = 'portfolio_item_6'),
    url(r'^portfolio_item_7/$',portfolio_item_7,name = 'portfolio_item_7'),
    url(r'^portfolio_item_8/$',portfolio_item_8,name = 'portfolio_item_8'),
    url(r'^portfolio_item_9/$',portfolio_item_9,name = 'portfolio_item_9'),
    url(r'^portfolio_item_10/$',portfolio_item_10,name = 'portfolio_item_10'),
    url(r'^portfolio_item_11/$',portfolio_item_11,name = 'portfolio_item_11'),
    url(r'^portfolio_item_12/$',portfolio_item_12,name = 'portfolio_item_12'),
    url(r'^university/$',university,name = 'university'),
    url(r'^user_profile_myemail/$',user_profile_myemail,name = 'user_profile_myemail'),
    url(r'^user_profile_mymessage/$',user_profile_mymessage,name = 'user_profile_mymessage'),
    url(r'^xiaoyuan/$',xiaoyuan,name = 'xiaoyuan'),
    url(r'^shipin/$',shipin,name = 'shipin'),
)
