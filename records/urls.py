from django.urls import path

from .views import(
    record_list_view,
    record_detail_view,
    record_create_view,
    record_update_view,
    record_delete_view,
)

app_name='records'

urlpatterns = [
    path('', record_list_view, name='list'),
    path('create/', record_create_view, name='create'),
    path('<slug:slug>/delete/', record_delete_view, name='delete'),
    path('<slug:slug>/update/', record_update_view, name='update'),
    path('<slug:slug>/', record_detail_view, name='detail'),
]