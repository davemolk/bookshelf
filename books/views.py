from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = [
        'title',
        'author',
        'notes',
        'cover_upload',
        'cover_url',
    ]
    labels = {
        'title': 'Book Title',
        'author': 'Author',
        'notes': 'My Notes',
        'cover_upload': 'Cover Image',
        'cover_url': 'Cover URL',
    }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = [
        'title',
        'author',
        'notes',
        'cover_upload',
        'cover_url',
    ]
    labels = {
        'title': 'Book Title',
        'author': 'Author',
        'notes': 'My Notes',
        'cover_upload': 'Cover Image',
        'cover_url': 'Cover URL',
    }
    action = 'Update'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')