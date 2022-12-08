from django.contrib import admin
from .models import Book,book_genre

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre']
    list_display_links = ['title', 'genre']

@admin.register(book_genre)
class book_genreAdmin(admin.ModelAdmin):
    list_display = ['genre']
    list_display_links = ['genre']
