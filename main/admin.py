from django.contrib import admin
from .models import Books, Python, Cplusplus, MLAI, Reviews
# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')

@admin.register(Python)
class PythonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')

@admin.register(Cplusplus)
class CplusplusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')

@admin.register(MLAI)
class MLAIAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city', 'review', 'rating')
