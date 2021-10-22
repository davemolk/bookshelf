from django.contrib.auth.mixins import LoginRequiredMixin
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
    template_name = 'books/book_list'

    # def get_queryset(self):
    #     return Book.objects.filter(owner=self.request.user)

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail'

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = [
        'title',
        'notes',
    ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = [
        'title',
        'notes',
    ]
    action = 'Update'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/'