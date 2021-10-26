from django.urls import path

from .views import(
    record_list_view,
    record_detail_view,
    record_create_view,
    record_update_view,
    record_delete_view,
    create_hx,
    detail_hx,
    update_hx,
    delete_hx,
)

app_name='records'

urlpatterns = [
    path('', record_list_view, name='list'),
    path('create/', record_create_view, name='create'),
    path('hx/create/', create_hx, name='create_hx'),
    path('hx/<slug:slug>/update', update_hx, name='update_hx'),
    path('hx/<slug:slug>/delete', delete_hx, name='delete_hx'),
    path('hx/<slug:slug>/', detail_hx, name='detail_hx'),
    path('<slug:slug>/delete/', record_delete_view, name='delete'),
    path('<slug:slug>/update/', record_update_view, name='update'),
    path('<slug:slug>/', record_detail_view, name='detail'),
]