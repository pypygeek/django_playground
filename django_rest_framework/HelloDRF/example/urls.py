from django.urls import path, include
from .views import HelloAPI, BooksAPI, BookAPI

urlpatterns = [
    path('hello/', HelloAPI.as_view()),
    path('books/', BooksAPI.as_view()),
    path('book/<int:bid>/', BookAPI.as_view()),
]
