from django.urls import path
from . import views

app_name = 'AccountsApp'

urlpatterns = [
    path('', views.LoginView, name = 'login'),
    path('logout/', views.LogoutView, name = 'logout')
]
