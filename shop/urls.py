from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage, name="HomePage"),
    path('Home/', views.HomePage, name='HomeShop'),
    path('about/', views.about, name='aboutUs'),
    path('contact/', views.contact, name='contactUs'),
    path('Products/<int:Proid>', views.Productview, name='Product Views'),
    path('Placeorder/', views.Placeorder, name='checked Out'),
    path('search/', views.search, name='Search'),
    path('register/', views.register, name='Registration Form'),
    path('LogIn/', views.LogIn, name='LogIn Form'),
    path('LogOut/', views.LogOut, name='LogOut Form'),
]
