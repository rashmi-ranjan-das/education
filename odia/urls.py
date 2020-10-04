"""odia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('explore/', views.explore, name='explore'),
    path('resources/', views.resources, name='resources'),
    path('articles/', views.articles, name='articles'),
    path('our_team/', views.team, name='team'),
    path('privacy/', views.privacy, name='privacy'),
    path('articles/python/i1001', views.pi1001, name='python1'),
    path('articles/python/i1002', views.pi1002, name='python2'),
    path('articles/python/i1003', views.pi1003, name='python3'),
    path('articles/c++/i1001', views.ci1001, name='c++1'),
    path('articles/c++/i1002', views.ci1002, name='c++2'),
    path('articles/c++/i1003', views.ci1003, name='c++3'),
    path('articles/mlai/i1001', views.mli1001, name='ml1'),
    path('articles/mlai/i1002', views.mli1002, name='ml2'),
    path('articles/mlai/i1003', views.mli1003, name='ml3'),
    path('articles/webdev/i1001', views.webi1001, name='web1'),
    path('articles/webdev/i1002', views.webi1002, name='web2'),
    path('articles/webdev/i1003', views.webi1003, name='web3'),
    path('contact/mail', views.mail, name="mail"),
    path('donation/', views.donation, name="donation"),
]
