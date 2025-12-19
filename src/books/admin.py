from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'category',
        'total_copies',
        'available_copies',
        'is_active',
        'created_at'
    )
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'author')
