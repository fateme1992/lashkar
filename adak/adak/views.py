
from django.shortcuts import HttpResponse


def Home_page(request):

    return HttpResponse("this is my first view")