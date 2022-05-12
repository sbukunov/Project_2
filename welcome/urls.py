
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.IndexView.as_view()),
]
