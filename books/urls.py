from django.contrib import admin
from django.urls import path
from .views import create_book, book_list, update_book, delete_book

urlpatterns = [
    path('',book_list,name='book_list'),
    path('create/',create_book,name='create_book'),
    path('update/<int:pk>/',update_book,name='update_book'),
    path('delete/<int:pk>/',delete_book,name='delete_book'),

]