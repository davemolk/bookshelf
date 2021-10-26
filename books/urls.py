from django.urls import path

from .views import (
    BookListView, 
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    SearchResultsListView,
)


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('add/', BookCreateView.as_view(), name='book_add'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('<slug:slug>/delete/', BookDeleteView.as_view(), name='book_confirm_delete'),
    path('<slug:slug>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
]