from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def test(request,art_id):
    return HttpResponse("Hello, world. You're at the article index.")


