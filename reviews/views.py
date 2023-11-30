from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .forms import ReviewForm

from .models import Review

# Create your views here.


# def review(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return render(request, 'reviews/review.html', {'form': form, 'review': review})
#     else:
#         form = ReviewForm()
#     return render(request, 'reviews/review.html', {'form': form})


class ReviewView(View):
    template_name = 'reviews/review.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = ReviewForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


# def all_reviews(request: HttpRequest) -> HttpResponse:
#     reviews = Review.objects.all()
#     return render(request, 'reviews/all_reviews.html', {'reviews': reviews})
class ReviewListView(ListView):
    template_name = 'reviews/all_reviews.html'
    model = Review
    context_object_name = 'reviews'
