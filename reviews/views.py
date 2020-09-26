from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from . import forms
from .models import Review
from books.models import Book
from movies.models import Movie


def add_review_book(request, pk):
  user = request.user
  if user.is_authenticated:
    form = forms.CreateReview(request.POST)
    try:
      book = Book.objects.get(pk=pk)
      if form.is_valid():
        review = form.save()
        review.book = book
        review.created_by = user
        review.save()
        return redirect(reverse("core:home"))
      else:
        return redirect(reverse("core:home"))
    except Book.DoesNotExist:
      return redirect(reverse("core:home"))
  return redirect(reverse("core:home"))

def add_review_movie(request, pk):
  user = request.user
  if user.is_authenticated:
    form = forms.CreateReview(request.POST)
    try:
      movie = Movie.objects.get(pk=pk)
      if form.is_valid():
        review = form.save()
        review.movie = movie
        review.created_by = user
        review.save()
        return redirect(reverse("core:home"))
      else:
        return redirect(reverse("core:home"))
    except Movie.DoesNotExist:
      return redirect(reverse("core:home"))
  return redirect(reverse("core:home"))

def delete_review(request,pk):
  review = Review.objects.get(pk=pk)
  review.delete()
  return redirect(reverse("core:home"))

def ReviewBookListView(request,pk):
  book = Book.objects.get(pk=pk)
  reviews = Review.objects.filter(book__pk=pk)
  form = forms.CreateReview()
  return render(request,"reviews/review_book_list.html",{"reviews":reviews,"book":book,"form":form})

def ReviewMovieListView(request,pk):
  movie = Movie.objects.get(pk=pk)
  reviews = Review.objects.filter(movie__pk=pk)
  form = forms.CreateReview()
  return render(request,"reviews/review_movie_list.html",{"reviews":reviews,"movie":movie,"form":form})