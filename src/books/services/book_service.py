from ..models import Book
from django.shortcuts import get_object_or_404

def list_available_books():
    """
    Return only active books with available copies
    """
    return Book.objects.filter(
        is_active=True,
        available_copies__gt=0
    )


def create_book(data):
    """
    Create a new book
    """
    return Book.objects.create(**data)


def update_book(book_id, data):
    """
    Update book details
    """
    book = get_object_or_404(Book, id=book_id)
    for field, value in data.items():
        setattr(book, field, value)
    book.save()
    return book


def delete_book(book_id):
    """
    Soft delete a book
    """
    book = get_object_or_404(Book, id=book_id)
    book.is_active = False
    book.save()
    return book
