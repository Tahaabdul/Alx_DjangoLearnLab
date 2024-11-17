from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register



urlpatterns = [
    path('books/', list_books, name='list_books'), # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('register/', register, name='register'),  # URL for registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # LoginView with template
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # LogoutView with template
]