from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book
from .models import Library  


# ✅ Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# ✅ Class-based view for displaying a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_object(self):
        library_id = self.kwargs.get("pk")
        return get_object_or_404(Library, pk=library_id)

