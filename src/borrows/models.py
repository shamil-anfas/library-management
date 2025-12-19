from django.db import models
from django.conf import settings
from books.models import Book  # if Book is in same app, adjust import

User = settings.AUTH_USER_MODEL


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    borrowed_at = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} borrowed {self.book}"
