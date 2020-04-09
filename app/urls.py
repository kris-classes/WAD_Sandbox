from django.urls import include, path

from django.http import HttpResponse, JsonResponse
from . import views


urlpatterns = [
    path('hello', views.hello),
    path('cars', views.list_cars),
]
