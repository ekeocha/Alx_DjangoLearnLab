from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Creation (optional, for testing) ---
author = Author.objects.get(name=author_name)  
books_by_author = Book.objects.filter(author=author)

book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

library = Library.objects.create(name="Central Library")
library.books.set([book1, book2])

librarian = Librarian.objects.get(library=library)
librarian = Librarian.objects.create(name="John Doe", library=library)
library = Library.objects.get(name=library_name)

# --- Queries ---
# 1. Query all books by a specific author
print("Books by George Orwell:")
for book in author.books.all():
    print(book.title)

# 2. List all books in a library
print("\nBooks in Central Library:")
for book in library.books.all():
    print(book.title)

# 3. Retrieve the librarian for a library
print("\nLibrarian of Central Library:")
print(library.librarian.name)
