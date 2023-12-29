from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('all/', views.ReviewListView.as_view(), name='all_reviews'),
    path('thank-you/', views.ThankYouView.as_view(), name='thank_you'),
    path('<int:pk>', views.ReviewDetails.as_view(), name='review_details'),
]
