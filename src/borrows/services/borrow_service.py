from django.utils import timezone
from django.db import transaction
from books.models import Book
from borrows.models import Borrow

from django.core.exceptions import ValidationError


class BorrowService:

    @staticmethod
    @transaction.atomic
    def borrow_book(user, book_id):
        """
        Borrow a book
        """

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise ValidationError("Book not found")

        # Check availability
        if book.available_copies <= 0:
            raise ValidationError("No copies available")

        # Create borrow record
        borrow = Borrow.objects.create(
            user=user,
            book=book
        )

        # Update book availability
        book.available_copies -= 1
        book.save()

        return borrow

    @staticmethod
    @transaction.atomic
    def return_book(user, borrow_id):
        """
        Return a borrowed book
        """

        try:
            borrow = Borrow.objects.get(id=borrow_id, user=user)
        except Borrow.DoesNotExist:
            raise ValidationError("Borrow record not found")

        if borrow.is_returned:
            raise ValidationError("Book already returned")

        # Mark as returned
        borrow.is_returned = True
        borrow.return_date = timezone.now()
        borrow.save()

        # Increase book availability
        book = borrow.book
        book.available_copies += 1
        book.save()

        return borrow
