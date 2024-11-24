from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.

def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    context = {'books': books}  # Pass the books to the template through the context

    return render(request, 'relationship_app/list_books.html', context=context)
    

class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get default context
        library = self.get_object()  # Get the library object (automatically handled by DetailView)
        context['books'] = library.books.all()  # Fetch all books related to this library
        return context