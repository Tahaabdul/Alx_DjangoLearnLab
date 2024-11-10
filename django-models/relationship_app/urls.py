from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # URL for registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # LoginView with template
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # LogoutView with template
]