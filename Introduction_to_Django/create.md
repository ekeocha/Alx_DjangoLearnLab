from bookshelf.models import book

book = Book.objects.create(title= "1984", author="George Orwell", publication_year=1949)
book.id

#Book instance created successfully with ID (e.g., 1)
