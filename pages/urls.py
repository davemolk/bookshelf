from django.urls import path
from .views import (
    HomePageView, 
    AboutPageView,
    SiteSearchResults,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('search/', SiteSearchResults.as_view(), name='all_search_results'),
]