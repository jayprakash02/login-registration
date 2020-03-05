from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url('index/',views.index,name='index'),
    url('special/',views.special,name='special'),
    url('login/',include('login.urls')),
    url('logout/', views.user_logout, name='logout'),
]
