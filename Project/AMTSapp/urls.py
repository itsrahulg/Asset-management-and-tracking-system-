from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage, name=""),
    path('login', views.login_view, name="login"),
    path('signup',views.signup_view,name="signup"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard',views.dashboard_view,name="dashboard"),
    path('addAsset',views.add_asset,name="addAsset"),
    path('log',views.updatelog,name="log"),
    path('google-login/', views.google_login, name='google_login'),
    path('oauth2callback/', views.google_callback, name='google_callback'),
    path('adduser',views.adduser,name="adduser"),
    path('create-superuser/', views.create_superuser, name='create_superuser'),
     path('assets/<str:location>/', views.assets_by_location, name='assets_by_location'),
    
]