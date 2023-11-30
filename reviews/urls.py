from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('all/', views.ReviewListView.as_view(), name='all_reviews'),
]
