from django.urls import include, path

from django.http import HttpResponse, JsonResponse
from . import views


urlpatterns = [
    path('hello', views.hello),
    path('cars', views.list_cars),
    path('car/<int:pk>/', views.CarDetailView.as_view()),
    path('car/all/', views.CarListView.as_view()),
]
