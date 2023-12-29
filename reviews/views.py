from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, FormView
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


# class ReviewView(View):
#     template_name = 'reviews/review.html'

#     def get(self, request: HttpRequest) -> HttpResponse:
#         form = ReviewForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request: HttpRequest) -> HttpResponse:
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, self.template_name, {'form': form})
#         return render(request, self.template_name, {'form': form})


class ReviewView(FormView):
    template_name = 'reviews/review.html'
    form_class = ReviewForm
    success_url = 'thank-you/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get(self, request: HttpRequest) -> HttpResponse:
    #     form = ReviewForm()
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request: HttpRequest) -> HttpResponse:
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, self.template_name, {'form': form})
    #     return render(request, self.template_name, {'form': form})


# def all_reviews(request: HttpRequest) -> HttpResponse:
#     reviews = Review.objects.all()
#     return render(request, 'reviews/all_reviews.html', {'reviews': reviews})

# generic list view
class ReviewListView(ListView):
    template_name = 'reviews/all_reviews.html'
    model = Review
    context_object_name = 'reviews'


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        # must call super() to get the context data
        context = super().get_context_data(**kwargs)

        context['message'] = 'This works!'
        return context

    # def get(self, request: HttpRequest) -> HttpResponse:
    #     return render(request, self.template_name)


# class ReviewDetails(TemplateView):
#     template_name = 'reviews/detail-review.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['pk']
#         selected_review = Review.objects.get(pk=review_id)
#         context['review'] = selected_review
#         return context

# generic detail view


class ReviewDetails(DetailView):
    template_name = 'reviews/detail-review.html'
    model = Review
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['pk']
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context
