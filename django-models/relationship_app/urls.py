from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.register, name='register'),  # URL for registration
    path('login/', views.user_login, name='login'),  # URL for login
    path('logout/', views.user_logout, name='logout'),  # URL for logout
]
