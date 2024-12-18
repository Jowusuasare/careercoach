from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #print(request.user)
    return HttpResponse("Hello, %s. Curious about career development? You're at the right place!" % request.user)

# def detail(request, question_id):
#     return HttpResponse("Hello, %s. Curious about career development? You're at the right place." % request.user)
