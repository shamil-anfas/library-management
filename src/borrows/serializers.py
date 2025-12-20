from rest_framework import serializers
from .models import Borrow


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = [
            'id',
            'user',
            'book',
            'borrowed_at',
            'return_date',
            'is_returned'
        ]
        read_only_fields = ['borrowed_at', 'return_date', 'is_returned']
