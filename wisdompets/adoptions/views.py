from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>home view</p>')

def pet_detail(request, id):
    return HttpResponse('<p>pet_detail view wit the id {}</p>'.format(id))

# Create your views here.
