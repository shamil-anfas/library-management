from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import BookSerializer
from .services.book_service import (
    list_available_books,
    create_book,
    update_book,
    delete_book
)


class BookListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        books = list_available_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        book = create_book(serializer.validated_data)
        return Response(
            BookSerializer(book).data,
            status=status.HTTP_201_CREATED
        )


class BookUpdateDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, book_id):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        book = update_book(book_id, serializer.validated_data)
        return Response(BookSerializer(book).data)

    def delete(self, request, book_id):
        delete_book(book_id)
        return Response(
            {"message": "Book removed successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
