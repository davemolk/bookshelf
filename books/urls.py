from django.urls import path

from .views import (
    BookListView, 
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('add/', BookCreateView.as_view(), name='book_add'),
    path('<slug:slug>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('<slug:slug>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
]