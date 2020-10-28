from django.contrib import admin
from .models import Books, Python, Cplusplus, MLAI, Reviews, Arduino, Quotes, WebDev
# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')

@admin.register(WebDev)
class WebDevAdmin(admin.ModelAdmin):
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

@admin.register(Arduino)
class ArduinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city', 'review', 'rating', 'time')

@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('id','quote', 'name',)
