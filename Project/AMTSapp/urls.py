from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage, name=""),
    path('login', views.login_view, name="login"),
    path('signup',views.signup_view,name="signup"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard',views.dashboard_view,name="dashboard"),
    
    path('log',views.updatelog,name="log"),
    path('google-login/', views.google_login, name='google_login'),
    path('oauth2callback/', views.google_callback, name='google_callback'),
    path('adduser',views.adduser,name="adduser"),
    path('users/', views.user_list_and_update, name='user_list_and_update'),
   
   
    path('assets/<str:location>/', views.assets_by_location, name='assets_by_location'),
    path('asset-types/', views.asset_types, name='asset_types'),
    

    path('software/', views.software_form, name='software_form'),
    path('software/update/<int:pk>/', views.update_software, name='update_software'),
    path('software/update-log/', views.software_update_log, name='software-update-log'),


    path('add_computer_hardware/', views.add_computer_hardware, name='add_computer_hardware'),
    path('computer-hardware/update/<int:pk>/', views.update_computer_hardware, name='update-computer-hardware'),
    path('computer-hardware/update-log/', views.computer_hardware_update_log, name='computer-hardware-update-log'),


    path('add_projector/', views.add_projector, name='add_projector'),
    path('update-projector/<int:id>/', views.update_projector, name='update-projector'),
    path('projector-update-log/', views.projector_update_log, name='projector-update-log'),


    path('add_book/', views.add_book, name='add_book'),
    path('books/update/<int:pk>/', views.update_book, name='update_book'),
    path('books/update-log/', views.book_update_log, name='book_update_log'),




    path('add_peripheral/', views.add_peripheral, name='add_peripheral'),
    path('peripherals/update/<int:pk>/', views.update_computer_peripheral, name='update_computer_peripheral'),
    path('peripherals/update-logs/', views.all_peripheral_update_logs, name='all_peripheral_update_logs'),

] 


