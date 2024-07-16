from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name=""),
    path('login', views.login, name="login"),
    path('signup',views.signup,name="signup"),
    path('userdashboard',views.user_dashboard,name="userdashboard"),
    path('administratordashboard',views.administrator_dashboard,name="administratordashboard"),
]