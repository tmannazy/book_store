from django.urls import path

from . import views

app_name = "book_store"

urlpatterns = [
	path("", views.index, name="index"),
	path("<int:pk>", views.publisher_details, name="publisher_details"),
	path("books/", views.book_list, name="books-book-list")

]