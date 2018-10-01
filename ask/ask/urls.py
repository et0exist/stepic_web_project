from django.conf.urls import url
from django.contrib import admin
from qa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login_, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^question/(?P<slug>\w+)/$', views.get_question, name='question'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^popular/', views.popular, name='popular'),
]
