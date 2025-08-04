from bookshelf.models import book

book = Book.objects.get(id=1)
book.delete()
Book.objects.all()

#expected output

The book instance is deleted.
