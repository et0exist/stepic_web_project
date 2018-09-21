"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from qa import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.home),
    re_path(r'^login/', views.login),
    re_path(r'^signup/', views.signup),
    re_path(r'^question/', views.question),
    re_path(r'^ask/', views.ask),
    re_path(r'^popular/', views.popular),
    re_path(r'^new/', views.new),
]
