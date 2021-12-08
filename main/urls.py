from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('?search=<str:search>/', views.search, name='search'),
    path('logout/', views.logoutUser, name="logout")
]


