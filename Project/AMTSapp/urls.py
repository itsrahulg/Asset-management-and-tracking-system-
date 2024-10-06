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
    path('scrapped-log/',views.scrapped_log,name="scrapped-log"),
    path('movement_history/',views.movement_history,name="movement_history"),
    path('location/<str:location>/user/', views.assets_by_location_user, name='assets_by_location_user'),

  
    

    path('software/', views.software_form, name='software_form'),
    path('software/update/<int:pk>/', views.update_software, name='update_software'),
    path('software/update-log/', views.software_update_log, name='software-update-log'),
    path('confirm_invalid_entry/<int:asset_id>/', views.confirm_invalid_entry, name='confirm_invalid_entry'),
    path('confirm_scrapped_asset/<int:asset_id>/', views.confirm_scrapped_asset, name='confirm_scrapped_asset'),
    path('invalid-software-entries/', views.invalid_software_entries, name='invalid_software_entries'),
    path('scrapped-software-assets/', views.scrapped_software_assets, name='scrapped_software_assets'),
    path('software/<int:id>/move/', views.move_software, name='move_software'),
    path('moved-software/', views.moved_software_list, name='moved_software_list'),



    path('add_computer_hardware/', views.add_computer_hardware, name='add_computer_hardware'),
    path('computer-hardware/update/<int:pk>/', views.update_computer_hardware, name='update-computer-hardware'),
    path('computer-hardware/update-log/', views.computer_hardware_update_log, name='computer-hardware-update-log'),
    path('hardware/invalid/<int:asset_id>/', views.confirm_invalid_computer_hardware, name='confirm_invalid_computer_hardware'),
    path('hardware/scrapped/<int:asset_id>/', views.confirm_scrapped_computer_hardware, name='confirm_scrapped_computer_hardware'),
    path('invalid-computer-hardware/', views.invalid_computer_hardware, name='invalid_computer_hardware'),
    path('scrapped-computer-hardware/', views.scrapped_computer_hardware, name='scrapped_computer_hardware'),
    path('hardware/move/<int:asset_id>/', views.move_computer_hardware, name='move_computer_hardware'),
    path('hardware/moved/', views.moved_computer_hardware_list, name='moved_computer_hardware_list'),



    path('add_projector/', views.add_projector, name='add_projector'),
    path('update-projector/<int:id>/', views.update_projector, name='update-projector'),
    path('projector-update-log/', views.projector_update_log, name='projector-update-log'),
    path('projectors/invalid/', views.invalid_projector_log, name='invalid-projector-log'),
    path('projectors/scrapped/', views.scrapped_projector_log, name='scrapped-projector-log'),
    path('projectors/invalid/<int:asset_id>/', views.invalid_projector, name='confirm_invalid_projector'),
    path('projectors/scrapped/<int:asset_id>/', views.scrapped_projector, name='confirm_scrapped_projector'),
    path('projectors/<int:id>/move/', views.move_projector, name='move_projector'),
    path('projectors/moved/', views.moved_projector_list, name='moved_projector_list'),


    path('add_book/', views.add_book, name='add_book'),
    path('books/update/<int:pk>/', views.update_book, name='update_book'),
    path('books/update-log/', views.book_update_log, name='book_update_log'),
    path('books/invalid/<int:asset_id>/', views.invalid_book, name='invalid_book'),
    path('books/scrapped/<int:asset_id>/', views.scrapped_book, name='scrapped_book'),
    path('books/invalid/', views.list_invalid_books, name='list_invalid_books'),
    path('books/scrapped/', views.list_scrapped_books, name='list_scrapped_books'),
    path('move_book/<int:pk>/', views.move_book, name='move_book'),
    path('moved_books/', views.moved_books_list, name='moved_books_list'),




    path('add_peripheral/', views.add_peripheral, name='add_peripheral'),
    path('peripherals/update/<int:pk>/', views.update_computer_peripheral, name='update_computer_peripheral'),
    path('peripherals/update-logs/', views.all_peripheral_update_logs, name='all_peripheral_update_logs'),
    path('move-to-invalid-computer-peripherals/<int:asset_id>/', views.move_to_invalid_computer_peripherals, name='move_to_invalid_computer_peripherals'),
    path('move-to-scrapped-computer-peripherals/<int:asset_id>/', views.move_to_scrapped_computer_peripherals, name='move_to_scrapped_computer_peripherals'),
    path('invalid-computer-peripherals/', views.invalid_computer_peripherals_list, name='invalid_computer_peripherals_list'),
    path('scrapped-computer-peripherals/', views.scrapped_computer_peripherals_list, name='scrapped_computer_peripherals_list'),
    path('move_peripheral/<int:pk>/', views.move_peripheral, name='move_peripheral'),
    path('moved_peripherals/', views.moved_peripherals_list, name='moved_peripherals_list'),



    path('add-furniture/', views.add_furniture, name='add_furniture'),

] 


