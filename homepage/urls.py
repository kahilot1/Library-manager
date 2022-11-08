from django.urls import path
from . import views
urlpatterns = [
    path("", views.mainScreen, name='main-selection-page'),
    path("addbook/", views.addBook, name='adding-book-page'),
    path('booklist/', views.listBook, name='viewing-book-page'),
]