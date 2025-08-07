from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Creation (optional, for testing) ---
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

library = Library.objects.create(name="Central Library")
library.books.set([book1, book2])

librarian = Librarian.objects.create(name="John Doe", library=library)

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
