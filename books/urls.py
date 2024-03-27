# books/urls.py
from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('<isbn>/', BookRetrieveUpdateDeleteAPIView.as_view(),
         name='book-retrieve-update-delete'),
]
