from django.urls import path,include ,re_path
from core import views

urlpatterns = [
    path('',views.index,name='Dashboard'),
    path('Manage/',views.manage,name='Manage'),
    re_path('Orders/',views.orders,name='orders'),
    path('Profile/',views.profile,name='Profile'),
    path('Contact/',views.contact,name='Contact'),
    path('Logout/',views.logout,name='Logout'),
    path('Vendors/',views.vendors,name='vendors'),
    path('license/',views.license_order,name='home'),
    path('edit',views.Edit,name='edit'),
    path('update/<str:id>',views.Update,name="update"),

   
]