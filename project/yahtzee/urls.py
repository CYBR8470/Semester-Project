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
<<<<<<< HEAD
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include         
=======
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
>>>>>>> 08f0fa1412f88c413e3432988458b8ab1e27f763
from django.contrib.auth import views as auth_views
from .frontend import views
from yahtzee.api import controllers

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('game/<str:choice>', views.game, name='game'),
    path('join/<str:gameid>', views.join, name='join'),
=======
    path('gameSetup/<str:choice>', views.gameSetup, name='gameSetup'),
    path('board/<str:gameid>', views.board, name='board'),
>>>>>>> 08f0fa1412f88c413e3432988458b8ab1e27f763
    path('end/', views.endgame, name='end'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register_request, name='register'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/games', controllers.GameList.as_view()),
]
=======
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 08f0fa1412f88c413e3432988458b8ab1e27f763
