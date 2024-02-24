"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('blog/',views.blog),
    path('shop/', views.shop ),
    path('test/', views.test),
    path('form/',views.form),
    path('submitform/',views.submitform,
    name="submitform"),
    path('calculate/',views.calculate),
    path('evenodd/',views.evenodd),
    path('marksheet/',views.marksheet),
    path('newsdetail/<newsid>',views.newsdetail),
    

    
    
]
