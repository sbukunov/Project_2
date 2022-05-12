
from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.RandomView.as_view()),
]
