
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]

class SearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100)

    def clean_q(self):
        # Extra basic normalization & validation if you want
        return self.cleaned_data["q"].strip()
