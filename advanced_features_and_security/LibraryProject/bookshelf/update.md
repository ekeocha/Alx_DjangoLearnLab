from lbookshelf.models import Book

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
book.title

#expected Output
Expected Output:
'Nineteen Eighty-Four
