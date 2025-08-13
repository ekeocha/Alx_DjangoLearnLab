from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import BookForm, SearchForm


@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    # form handling logic here
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # edit logic here
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'relationship_app/delete_success.html')

@permission_required('relationship_app.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})




@login_required
def book_list(request):
    """
    Safe search using Django ORM to avoid SQL injection.
    """
    form = SearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            books = books.filter(Q(title__icontains=q) | Q(author__icontains=q))
    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
@require_http_methods(["GET", "POST"])
def create_book(request):
    """
    Uses ModelForm + CSRF token in template. No raw SQL.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})

@login_required
@require_http_methods(["GET", "POST"])
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form})

@login_required
@require_http_methods(["POST"])
def delete_book(request, pk):
    """
    Deletes via POST only (no GET deletes).
    """
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")


# Example of safe raw SQL if you must use it:
from django.db import connection

@login_required
def search_books_raw_sql_example(request):
    """
    Avoid building SQL via string interpolation.
    Use params with cursor.execute(sql, [params...]).
    """
    books = []
    form = SearchForm(request.GET or None)
    if form.is_valid():
        q = form.cleaned_data.get("q") or ""
        sql = "SELECT id, title, author, published_date FROM bookshelf_book WHERE title LIKE %s"
        with connection.cursor() as cursor:
            cursor.execute(sql, [f"%{q}%"])
            rows = cursor.fetchall()
        # rows -> hydrate manually (or use ORM wherever possible)
        for (pk, title, author, published_date) in rows:
            books.append({"id": pk, "title": title, "author": author, "published_date": published_date})
    return render(request, "bookshelf/book_list.html", {"books": books})
