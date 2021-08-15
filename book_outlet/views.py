from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Min, Max

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('-rating', "title")
    return render(request, "book_outlet/index.html", {
        "books" : books,
        "count": books.count(),
        "avg_rating": books.aggregate(Avg("rating"), Min("rating"), Max("rating"))  # rating__avg, rating__min, rating__max
    })


def book_detail(request, slug):
    book = None
    # try:
    #     book = Book.objects.get(pk=b_id)
    # except Book.DoesNotExist:
    #     print(f"No Book available with ID: {b_id}")
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "book": book
    })



