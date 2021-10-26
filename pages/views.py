from django.views.generic import (
    TemplateView,
    ListView,
)
from django.db.models import Q
from itertools import chain
from books.models import Book
from records.models import Record


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class SiteSearchResults(ListView):
    model = Book
    template_name = 'search_results.html'

    # def get_context_data(self, **kwargs):
    #     context = super(SiteSearchResults, self).get_context_data(**kwargs)
    #     context['record_list'] = Record.objects.all()
    #     return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        book_results = Book.objects.filter(owner=self.request.user).filter(
            Q(title__icontains=query) | Q(author__icontains=query)
            | Q(notes__icontains=query)
        ).order_by('title')
        record_results = Record.objects.filter(owner=self.request.user).filter(
             Q(title__icontains=query) | Q(musicians__icontains=query)
            | Q(notes__icontains=query)
        ).order_by('title')
        qs_chain = chain(book_results, record_results)
        return qs_chain