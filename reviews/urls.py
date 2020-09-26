from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
  path("<int:pk>", views.ReviewBookListView, name="book_list"),
  path("<int:pk>", views.ReviewMovieListView, name="movie_list"),
  path("add/<int:pk>",views.add_review_book,name="book_add"),
  path("add/<int:pk>",views.add_review_movie,name="movie_add"),
  path("remove/<int:pk>",views.delete_review,name="remove"),
]

