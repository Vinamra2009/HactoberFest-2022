from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add-a-book',views.add_a_book),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('about-us/', views.aboutus, name="aboutus"),
]
