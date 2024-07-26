from django.urls import path
from . import views
from .views import register_view,login_view,register_table_view

urlpatterns = [
	path('register/', views.UserRegister.as_view(), name='register'),
    path('registerform', register_view, name='registerform'),
	path('login/', views.UserLogin.as_view(), name='login'),
    path('adminlogin/', login_view, name='adminlogin'),
    path('registertable/', register_table_view, name='register_table'),


	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
]