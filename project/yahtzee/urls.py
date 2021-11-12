"""yahtzee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .frontend import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<str:choice>', views.game, name='game'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login', auth_views.LoginView.as_view(template_name='login.html')),
    # path('login', views.loginUser, name='login'),
    path('register', views.register_request, name='register'),
    path('admin/', admin.site.urls),
]
