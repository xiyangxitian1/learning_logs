"""为应用程序users定义URL模式"""

# from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views

LoginView.template_name = 'users/login.html'
urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(), name='login'),
    # 注销
    path(r'^logout/$', views.logout_view, name='logout'),
    # 注册页面
    path(r'^register/$', views.register, name='register'),

]

app_name = 'users'
