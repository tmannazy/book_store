from django.urls import path

from . import views

app_name = "book_store"

urlpatterns = [
	path("", views.index, name="index")
]