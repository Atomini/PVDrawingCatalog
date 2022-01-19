from django.urls import path
from .views import show_book_tree, show_assembly_tree


urlpatterns = [
    path('12', show_book_tree, name='book'),
    path('1', show_assembly_tree, name='assembly'),
]