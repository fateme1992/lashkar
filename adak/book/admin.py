from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ["id","book_name","writer","year","pages"]
    list_editable = ("book_name","writer","year","pages")
    list_filter = ("year","writer")
    ordering = ("id",)
admin.site.register(Book,BookAdmin)