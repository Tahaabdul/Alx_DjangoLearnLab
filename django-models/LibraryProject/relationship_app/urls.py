from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('librarylist/<int:pk>/',views.LibraryListView.as_view(), name ="librarylist")
]