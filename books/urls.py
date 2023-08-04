from django.urls import path
from .views import BookListView
from .views import BookDetailView

app_name = 'books'

urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    # Other URL patterns for different views can go here if you have any.
    path('list/<pk>', BookDetailView.as_view(), name='detail'),
]