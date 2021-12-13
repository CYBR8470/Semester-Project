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
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from .frontend import views
from yahtzee.api import controllers

urlpatterns = [
    path('', views.index, name='index'),
    path('action/<str:gameid>/<str:action>', views.action, name='action'),
    path('join/<str:gameid>', views.join, name='join'),
    path('gameSetup/<str:choice>', views.gameSetup, name='gameSetup'),
    path('board/<str:gameid>', views.board, name='board'),
    path('end/', views.endgame, name='end'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register_request, name='register'),
    path('admin/', admin.site.urls),
    path('api/games', controllers.GameList.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
