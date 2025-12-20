from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from borrows.services.borrow_service import BorrowService
from borrows.serializers import BorrowSerializer
from django.core.exceptions import ValidationError

class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book_id = request.data.get("book_id")

        if not book_id:
            return Response(
                {"error": "book_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            borrow = BorrowService.borrow_book(
                user=request.user,
                book_id=book_id
            )
        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BorrowSerializer(borrow)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        borrow_id = request.data.get("borrow_id")

        if not borrow_id:
            return Response(
                {"error": "borrow_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            borrow = BorrowService.return_book(
                user=request.user,
                borrow_id=borrow_id
            )
        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BorrowSerializer(borrow)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
