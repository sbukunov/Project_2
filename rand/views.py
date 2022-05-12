from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse
import random

class RandomView(View):
    def get(self, request:HttpRequest):
        random_number = f"{random.random()}"
        return HttpResponse(random_number)


# Create your views here.
